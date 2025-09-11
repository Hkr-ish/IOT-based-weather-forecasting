import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime, timedelta
import pickle
import os

class TemperatureForecaster:
    def __init__(self):
        self.model = None
        self.poly_features = PolynomialFeatures(degree=3)
        self.is_trained = False
        self._train_initial_model()
    
    def _train_initial_model(self):
        """Train initial model with synthetic data"""
        # Generate synthetic training data
        hours = np.arange(168)  # 1 week of hourly data
        # Create temperature pattern with multiple seasonalities
        temp = (25 +  # base temperature
                10 * np.sin(2 * np.pi * hours / 24) +  # daily pattern
                2 * np.sin(2 * np.pi * hours / (24*7)) +  # weekly pattern
                np.random.normal(0, 1, len(hours)))  # noise
        
        # Prepare features
        X = hours.reshape(-1, 1)
        X_poly = self.poly_features.fit_transform(X)
        y = temp
        
        # Train model
        self.model = LinearRegression()
        self.model.fit(X_poly, y)
        self.is_trained = True
    
    def train_model(self, historical_data):
        """Train model with actual historical data"""
        if len(historical_data) < 24:
            return False  # Not enough data
        
        # Convert to DataFrame
        df = pd.DataFrame(historical_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Create time-based features
        df['hour_index'] = (df['timestamp'] - df['timestamp'].min()).dt.total_seconds() / 3600
        df = df.sort_values('hour_index')
        
        # Prepare features and target
        X = df['hour_index'].values.reshape(-1, 1)
        X_poly = self.poly_features.fit_transform(X)
        y = df['temperature'].values
        
        # Train model
        self.model = LinearRegression()
        self.model.fit(X_poly, y)
        self.is_trained = True
        return True
    
    def get_forecast(self, hours_ahead=24):
        """Generate temperature forecast for specified hours ahead"""
        if not self.is_trained:
            self._train_initial_model()
        
        # Get last timestamp from training
        last_hour = 168  # default if no training data
        
        # Generate future timestamps
        future_hours = np.arange(last_hour, last_hour + hours_ahead)
        X_future = future_hours.reshape(-1, 1)
        X_future_poly = self.poly_features.transform(X_future)
        
        # Predict temperatures
        predictions = self.model.predict(X_future_poly)
        
        # Create forecast data
        forecast = []
        base_time = datetime.now()
        for i, temp in enumerate(predictions):
            timestamp = base_time + timedelta(hours=i+1)
            forecast.append({
                'timestamp': timestamp.isoformat(),
                'temperature': round(temp, 2),
                'confidence': 0.85  # Static confidence for now
            })
        
        return forecast