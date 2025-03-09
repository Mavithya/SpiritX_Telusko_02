from flask import request
from flask_socketio import SocketIO, emit, join_room
from bson import ObjectId, json_util
from services.database import mongo
import json
import logging

socketio = SocketIO(None, cors_allowed_origins="http://localhost:3000", logger=True, engineio_logger=True)

def serialize(data):
    """Serialize MongoDB documents to JSON"""
    return json.loads(json_util.dumps(data))

def watch_collection(collection_name, event_name):
    """Watch MongoDB collection changes and emit Socket.IO events"""
    try:
        with mongo.db[collection_name].watch(
            full_document='updateLookup',
            max_await_time_ms=1000
        ) as stream:
            logging.info(f"Watching {collection_name} collection for changes...")
            for change in stream:
                doc = change.get('fullDocument', {})
                doc['_id'] = str(doc['_id']) if '_id' in doc else None
                
                socketio.emit(event_name, {
                    'operation': change['operationType'],
                    'data': serialize(doc),
                    'change_id': str(change['_id'])
                })
                logging.debug(f"Emitted {event_name} event for {change['operationType']}")
    except Exception as e:
        logging.error(f"Change stream error for {collection_name}: {str(e)}")
        socketio.emit('error', {'message': f"Change stream error: {str(e)}"})

def watch_players():
    """Watch players collection changes"""
    watch_collection('players', 'player_update')

def watch_users():
    """Watch users collection changes"""
    watch_collection('users', 'user_update')

@socketio.on('connect')
def handle_connect():
    """Handle new client connections"""
    emit('connection_status', {'status': 'connected', 'sid': request.sid})
    logging.info(f"Client connected: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnections"""
    logging.info(f"Client disconnected: {request.sid}")

@socketio.on('subscribe')
def handle_subscribe(data):
    """Handle client subscription requests"""
    try:
        if data.get('collection') == 'players':
            join_room('players_updates')
        elif data.get('collection') == 'users':
            join_room('users_updates')
        
        emit('subscription_status', {
            'status': 'subscribed',
            'collection': data.get('collection')
        })
    except Exception as e:
        emit('error', {'message': str(e)})

def init_realtime(app):
    """Initialize real-time services"""
    global socketio
    socketio.init_app(app)  # 🔥 This ensures socketio is linked to Flask
    
    with app.app_context():
        # Start change stream watchers
        socketio.start_background_task(watch_players)
        socketio.start_background_task(watch_users)
        logging.info("Real-time services initialized")