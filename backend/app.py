from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from services.database import mongo, initialize_data
from services.realtime import socketio, init_realtime
from admin.routes import admin_bp
from user.routes import user_bp
from services.utils import update_player_values
from flask import Flask
from flask_cors import CORS
from extensions import bcrypt, jwt, socketio, mongo

app = Flask(__name__)
CORS(app, 
     resources={r"/admin/*": {
         "origins": ["http://localhost:5173"],
         "methods": ["GET", "POST", "PUT", "DELETE"],
         "allow_headers": ["Content-Type", "Authorization"]
     }},
     supports_credentials=True)
bcrypt.init_app(app)
app.config.from_object(Config)

# Initialize extensions
mongo.init_app(app)
with app.app_context():
    initialize_data(app)
    update_player_values()

jwt.init_app(app)
socketio.init_app(app, cors_allowed_origins="*")

init_realtime(app)

# Register blueprints
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)