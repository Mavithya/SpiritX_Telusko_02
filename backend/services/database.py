from extensions import mongo
from pymongo import ASCENDING, DESCENDING
import pandas as pd
import os
import logging


def initialize_data(app):
    """Initialize database with sample data if empty"""
    with app.app_context():
        try:
            # Create indexes
            app.logger.info("Creating database indexes...")
            mongo.db.players.create_index([("Name", ASCENDING)], unique=True)
            mongo.db.players.create_index([("Category", ASCENDING)])
            mongo.db.players.create_index([("value", DESCENDING)])
            mongo.db.users.create_index([("username", ASCENDING)], unique=True)

            # Insert sample players if collection is empty
            if mongo.db.players.count_documents({}) == 0:
                app.logger.info("Populating players collection...")
                
                # Load CSV data
                df = pd.read_csv('sample_data.csv')
                
                # Clean column names and data
                df.columns = [col.replace(' ', '_') for col in df.columns]
                df = df.where(pd.notnull(df), None)
                
                # Calculate and add derived fields
                players = []
                for _, row in df.iterrows():
                    # Batting calculations
                    batting_sr = row['Total_Runs'] / row['Balls_Faced'] * 100 if row['Balls_Faced'] else 0
                    batting_avg = row['Total_Runs'] / row['Innings_Played'] if row['Innings_Played'] else 0
                    
                    # Bowling calculations
                    balls_bowled = row['Overs_Bowled'] * 6 if row['Overs_Bowled'] else 0
                    bowling_sr = balls_bowled / row['Wickets'] if row['Wickets'] else 0
                    economy = (row['Runs_Conceded'] / balls_bowled) * 6 if balls_bowled else 0
                    
                    # Points and value
                    points = ((batting_sr / 5) + (batting_avg * 0.8)) + \
                            ((500 / batting_sr if batting_sr else 0) + (140 / economy if economy else 0))
                    value = round(((9 * points + 100) * 1000) // 50000 * 50000)
                    
                    player = {
                        **row.to_dict(),
                        "batting_sr": round(batting_sr, 2),
                        "batting_avg": round(batting_avg, 2),
                        "bowling_sr": round(bowling_sr, 2),
                        "economy": round(economy, 2),
                        "points": round(points, 2),
                        "value": value
                    }
                    players.append(player)

                # Insert into MongoDB
                result = mongo.db.players.insert_many(players)
                app.logger.info(f"Inserted {len(result.inserted_ids)} players")

            # Create default admin user if not exists
            if not mongo.db.users.find_one({"username": "admin"}):
                mongo.db.users.insert_one({
                    "username": "admin",
                    "password": "adminpassword",  # In production, use proper hashing
                    "role": "admin"
                })

        except FileNotFoundError:
            app.logger.error("sample_data.csv not found in project root directory")
        except Exception as e:
            app.logger.error(f"Database initialization failed: {str(e)}")

def get_db():
    """Get database instance"""
    return mongo.db

def create_players_view():
    """Create a view for player stats aggregation"""
    mongo.db.command({
        'create': 'player_stats',
        'viewOn': 'players',
        'pipeline': [
            {'$project': {
                'Name': 1,
                'University': 1,
                'Category': 1,
                'Total_Runs': 1,
                'Wickets': 1,
                'value': 1,
                'batting_sr': 1,
                'bowling_sr': 1
            }}
        ]
    })