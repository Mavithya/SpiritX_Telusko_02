import os
from datetime import timedelta

class Config:
    MONGO_URI = "mongodb://localhost:27017/fantasy_cricket"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET", "@SecretKey!123")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)