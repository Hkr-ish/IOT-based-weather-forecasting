# IoT-Based Temperature Forecasting System (Simulation-Driven Approach)

This project implements a simulation-driven IoT temperature forecasting system using Python and Flask. The system simulates temperature data from IoT sensors and uses machine learning to forecast future temperatures.

## Features
- Real-time temperature data simulation
- Machine learning-based temperature forecasting
- Interactive web dashboard with real-time visualization
- REST API for data access
- Historical data storage and retrieval

## Architecture
The system consists of several components:
1. Data Simulation Module - Generates realistic temperature data
2. Forecasting Engine - ML model for temperature prediction
3. Data Storage - Stores historical temperature data
4. REST API - Provides data access endpoints
5. Web Interface - Dashboard for visualization and control
6. Configuration Manager - Handles system settings

## Technologies Used
- Python 3.x
- Flask (Web Framework)
- Scikit-learn (Machine Learning)
- Pandas (Data Processing)
- NumPy (Numerical Computing)
- Chart.js (Data Visualization)
- SQLite (Data Storage)

## Setup and Installation

### 1. Create a Virtual Environment
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python run.py
```

After running the command, the application will be accessible at `http://localhost:5000` in your web browser.

## Project Overview

This is an IoT-Based Temperature Forecasting System that simulates temperature data from IoT sensors and uses machine learning to forecast future temperatures. The system provides a web interface to visualize real-time and historical temperature data, along with predictions.

## What Happens When You Run python run.py

1. Database Initialization
   - First, it checks if temperature_data.db exists
   - If not, it creates a SQLite database with a table for temperature readings
   - If it exists, it uses the existing database

2. Flask Web Application Startup
   - Creates a Flask application with CORS enabled
   - Sets up routing for different parts of the application:
     - Main dashboard page (/)
     - API endpoints for data (/api/*)

3. Web Server Launch
   - Starts a Flask development server on http://0.0.0.0:5000
   - Opens a web page in your browser showing the dashboard

## What the Web Page Shows

When you open the webpage, you'll see a dashboard with several sections:

1. Current Conditions Display:
   - Current temperature reading (simulated)
   - Current humidity level (simulated)
   - Current atmospheric pressure (simulated)

2. Temperature History Chart:
   - Line chart showing temperature readings over the past 24 hours
   - Updates automatically every 30 seconds

3. Temperature Forecast Chart:
   - Line chart showing predicted temperatures for the next 24 hours (default)
   - Can be adjusted to show forecasts for 12, 48, or 72 hours

4. System Controls:
   - Simulation settings where you can adjust:
     - Base temperature
     - Temperature amplitude (how much temperature varies)
   - Forecast controls to change the time range of predictions
   - Refresh button to manually update all data

## How the System Works

1. Data Simulation:
   - The system generates realistic temperature data based on:
     - Time of day patterns (warmer during the day, cooler at night)
     - Configurable base temperature and amplitude
     - Random noise to simulate real-world variations
   - Also simulates humidity and pressure readings

2. Data Storage:
   - All temperature readings are saved to the SQLite database
   - Historical data is used for forecasting

3. Machine Learning Forecasting:
   - Uses a polynomial regression model to predict future temperatures
   - Trained on either synthetic data or actual historical data
   - Makes predictions based on detected patterns in the data

4. REST API:
   - Provides endpoints for:
     - Current temperature data
     - Historical temperature data
     - Temperature forecasts
     - Simulation settings management

This system is particularly useful for:
- Testing IoT applications without physical hardware
- Demonstrating temperature forecasting concepts
- Learning about web development with Flask
- Understanding how machine learning can be applied to time series data