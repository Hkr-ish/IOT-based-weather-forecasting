# IoT-Based Temperature Forecasting System (Simulation-Driven Approach)

## System Overview

This project implements a simulation-driven IoT temperature forecasting system using Python and Flask. The system simulates temperature data from IoT sensors and uses machine learning to forecast future temperatures without requiring any hardware components.

## Features

- Real-time temperature data simulation
- Machine learning-based temperature forecasting
- Interactive web dashboard with real-time visualization
- REST API for data access
- Historical data storage and retrieval
- Configurable simulation parameters

## System Architecture

The system consists of several components:

1. **Data Simulation Module** - Generates realistic temperature data
2. **Forecasting Engine** - ML model for temperature prediction
3. **Data Storage** - Stores historical temperature data
4. **REST API** - Provides data access endpoints
5. **Web Interface** - Dashboard for visualization and control
6. **Configuration Manager** - Handles system settings

## Technologies Used

- Python 3.x
- Flask (Web Framework)
- Scikit-learn (Machine Learning)
- Pandas (Data Processing)
- NumPy (Numerical Computing)
- Chart.js (Data Visualization)
- SQLite (Data Storage)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd iobased
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python run.py
   ```

5. Access the dashboard at `http://localhost:5000`

## API Endpoints

### GET /api/temperature/current
Returns the current simulated temperature reading.

### GET /api/temperature/history?hours=N
Returns temperature history for the last N hours (default: 24).

### GET /api/temperature/forecast?hours=N
Returns temperature forecast for the next N hours (default: 24).

### GET /api/temperature/settings
Returns current simulation settings.

### POST /api/temperature/settings
Updates simulation settings. Accepts JSON with:
- base_temperature: Base temperature in Celsius
- amplitude: Temperature variation amplitude
- noise_level: Random noise level
- trend: Temperature trend
- seasonal_period: Seasonal period in hours

### GET /api/status
Returns system status information.

## System Components

### Data Simulation Module (`app/utils/data_simulator.py`)
Generates realistic temperature data using a sinusoidal model with configurable parameters:
- Base temperature
- Amplitude (daily temperature variation)
- Noise level (random variations)
- Trend (long-term temperature changes)
- Seasonal period

### Forecasting Engine (`app/models/forecaster.py`)
Uses polynomial regression to forecast future temperatures based on historical data.

### Data Storage (`temperature_data.db`)
SQLite database that stores all temperature readings with timestamps.

### Web Interface (`app/templates/index.html`)
Interactive dashboard showing:
- Current temperature, humidity, and pressure
- Temperature history chart
- Temperature forecast chart
- System controls for configuration

## Configuration

The system can be configured through `config.json`:
```json
{
    "simulation": {
        "update_interval": 60,
        "data_retention_days": 7
    },
    "forecasting": {
        "model_update_interval": 3600,
        "default_forecast_hours": 24
    },
    "web": {
        "refresh_interval": 30
    }
}
```

## Extending the System

### Adding New Sensors
To add new sensor types, modify the `TemperatureSimulator` class in `app/utils/data_simulator.py` to include additional parameters.

### Improving Forecasting
To improve forecasting accuracy, modify the `TemperatureForecaster` class in `app/models/forecaster.py` to use more advanced ML models.

### Custom Visualizations
To add new visualizations, modify `app/templates/index.html` and the corresponding JavaScript functions.

## Testing

Run the system and verify that:
1. The dashboard loads correctly
2. Current temperature updates regularly
3. Historical data is displayed in the chart
4. Forecast data is generated and displayed
5. Settings can be updated through the UI
6. API endpoints return correct data

## Troubleshooting

### Dashboard not loading
- Check that the Flask server is running
- Verify there are no error messages in the console
- Ensure all dependencies are installed

### No data in charts
- Check browser console for JavaScript errors
- Verify API endpoints are returning data
- Confirm the database is being populated

### Forecast seems inaccurate
- The model needs historical data to improve
- Adjust simulation parameters for more realistic data
- Consider implementing a more sophisticated ML model