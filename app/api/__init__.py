from flask import Blueprint, jsonify, request
from app.utils.data_simulator import TemperatureSimulator
from app.models.forecaster import TemperatureForecaster
import json
import sqlite3
import os
from datetime import datetime

bp = Blueprint('api', __name__)

# Initialize simulator and forecaster
simulator = TemperatureSimulator()
forecaster = TemperatureForecaster()

# Database setup
def init_db():
    db_path = 'temperature_data.db'
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS temperature_readings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT NOT NULL,
                  temperature REAL NOT NULL,
                  humidity REAL,
                  pressure REAL)''')
    conn.commit()
    conn.close()
    return db_path

DB_PATH = init_db()

def save_temperature_reading(reading):
    """Save temperature reading to database"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO temperature_readings (timestamp, temperature, humidity, pressure) VALUES (?, ?, ?, ?)",
              (reading['timestamp'], reading['temperature'], reading['humidity'], reading['pressure']))
    conn.commit()
    conn.close()

def get_temperature_history_db(hours=24):
    """Get temperature history from database"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Calculate the time threshold
    time_threshold = datetime.now().timestamp() - (hours * 3600)
    c.execute("SELECT timestamp, temperature, humidity, pressure FROM temperature_readings WHERE timestamp > datetime(?, 'unixepoch') ORDER BY timestamp",
              (time_threshold,))
    rows = c.fetchall()
    conn.close()
    
    history = []
    for row in rows:
        history.append({
            'timestamp': row[0],
            'temperature': row[1],
            'humidity': row[2],
            'pressure': row[3]
        })
    
    return history

@bp.route('/temperature/current')
def current_temperature():
    """Get current simulated temperature"""
    temp_data = simulator.get_current_temperature()
    # Save to database
    save_temperature_reading(temp_data)
    return jsonify(temp_data)

@bp.route('/temperature/history')
def temperature_history():
    """Get historical temperature data"""
    hours = request.args.get('hours', 24, type=int)
    # Try to get from database first
    try:
        history_data = get_temperature_history_db(hours)
        if not history_data:
            # Fallback to simulator if database is empty
            history_data = simulator.get_temperature_history(hours)
    except Exception as e:
        # Fallback to simulator if database error
        print(f"Database error: {e}")
        history_data = simulator.get_temperature_history(hours)
    
    return jsonify(history_data)

@bp.route('/temperature/forecast')
def temperature_forecast():
    """Get temperature forecast"""
    hours = request.args.get('hours', 24, type=int)
    forecast_data = forecaster.get_forecast(hours)
    return jsonify(forecast_data)

@bp.route('/temperature/settings', methods=['GET', 'POST'])
def temperature_settings():
    """Get or update temperature simulation settings"""
    if request.method == 'POST':
        settings = request.json
        simulator.update_settings(settings)
        return jsonify({"status": "success", "message": "Settings updated"})
    
    return jsonify(simulator.get_settings())