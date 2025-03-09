from services.database import mongo

def calculate_player_value(points):
    """Calculate player value based on points."""
    return round((9 * points + 100) * 1000 / 50000) * 50000

def update_player_values():
    """Ensure all players have a 'value' field."""
    if mongo.db is None:
        raise RuntimeError("MongoDB not initialized")
    
    players = mongo.db.players.find()
    for player in players:
        if 'value' not in player:
            points = player.get('points', 0)
            value = calculate_player_value(points)
            mongo.db.players.update_one(
                {'_id': player['_id']},
                {'$set': {'value': value}}
            )