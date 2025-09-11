from app import create_app
import os
import sqlite3

def init_db():
    """Initialize the database"""
    db_path = 'temperature_data.db'
    if not os.path.exists(db_path):
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
        print("Database initialized successfully")
    else:
        print("Database already exists")

app = create_app()

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)