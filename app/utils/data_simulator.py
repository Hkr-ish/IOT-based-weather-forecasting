import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

class TemperatureSimulator:
    def __init__(self):
        self.settings = {
            'base_temperature': 25.0,
            'amplitude': 10.0,
            'noise_level': 1.0,
            'trend': 0.0,
            'seasonal_period': 24
        }
        self.history = []
        self._initialize_history()
    
    def _initialize_history(self):
        """Initialize with 48 hours of historical data"""
        now = datetime.now()
        for i in range(48):
            timestamp = now - timedelta(hours=i)
            temp = self._generate_temperature(timestamp)
            self.history.append({
                'timestamp': timestamp.isoformat(),
                'temperature': temp,
                'humidity': 50 + random.uniform(-10, 10),
                'pressure': 1013 + random.uniform(-10, 10)
            })
        self.history.reverse()  # Oldest first
    
    def _generate_temperature(self, timestamp):
        """Generate realistic temperature based on time of day and settings"""
        # Convert timestamp to hour of day (0-23)
        hour = timestamp.hour
        
        # Sinusoidal pattern for daily temperature variation
        daily_pattern = np.sin(2 * np.pi * (hour - 6) / 24)
        
        # Base temperature with daily pattern
        temp = (self.settings['base_temperature'] + 
                self.settings['amplitude'] * daily_pattern +
                self.settings['trend'] +
                random.uniform(-self.settings['noise_level'], self.settings['noise_level']))
        
        return round(temp, 2)
    
    def get_current_temperature(self):
        """Generate new temperature reading"""
        now = datetime.now()
        temp = self._generate_temperature(now)
        
        reading = {
            'timestamp': now.isoformat(),
            'temperature': temp,
            'humidity': 50 + random.uniform(-10, 10),
            'pressure': 1013 + random.uniform(-10, 10)
        }
        
        # Add to history
        self.history.append(reading)
        
        # Keep only last 168 hours (1 week)
        if len(self.history) > 168:
            self.history.pop(0)
        
        return reading
    
    def get_temperature_history(self, hours=24):
        """Get temperature history for specified hours"""
        if hours >= len(self.history):
            return self.history
        
        return self.history[-hours:]
    
    def update_settings(self, settings):
        """Update simulation settings"""
        for key, value in settings.items():
            if key in self.settings:
                self.settings[key] = value
    
    def get_settings(self):
        """Get current simulation settings"""
        return self.settings