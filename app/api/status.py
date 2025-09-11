from flask import Blueprint, jsonify
from app.utils.data_simulator import TemperatureSimulator
from app.models.forecaster import TemperatureForecaster
from app.utils.config import ConfigManager
import os
import sqlite3

bp = Blueprint('status', __name__)

@bp.route('/status')
def system_status():
    """Get system status information"""
    config = ConfigManager()
    
    # Check database
    db_status = "OK"
    db_size = 0
    try:
        if os.path.exists('temperature_data.db'):
            db_size = os.path.getsize('temperature_data.db')
            conn = sqlite3.connect('temperature_data.db')
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM temperature_readings")
            row_count = c.fetchone()[0]
            conn.close()
        else:
            db_status = "Database not found"
            row_count = 0
    except Exception as e:
        db_status = f"Error: {str(e)}"
        row_count = 0
    
    # Get config info
    sim_config = config.get('simulation', 'update_interval', 60)
    web_config = config.get('web', 'refresh_interval', 30)
    
    status_info = {
        "system_status": "Operational",
        "database": {
            "status": db_status,
            "size_bytes": db_size,
            "record_count": row_count
        },
        "configuration": {
            "simulation_update_interval": sim_config,
            "web_refresh_interval": web_config
        },
        "simulator": {
            "status": "Active",
            "settings": TemperatureSimulator().get_settings()
        },
        "forecaster": {
            "status": "Trained",
            "model_status": "Ready"
        }
    }
    
    return jsonify(status_info)