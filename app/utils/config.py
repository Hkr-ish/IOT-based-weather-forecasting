import json
import os

class ConfigManager:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.default_config = {
            'simulation': {
                'update_interval': 60,  # seconds
                'data_retention_days': 7
            },
            'forecasting': {
                'model_update_interval': 3600,  # seconds
                'default_forecast_hours': 24
            },
            'web': {
                'refresh_interval': 30  # seconds
            }
        }
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from file or use defaults"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    for key, value in self.default_config.items():
                        if key not in config:
                            config[key] = value
                    return config
            except Exception:
                return self.default_config
        return self.default_config
    
    def save_config(self):
        """Save current configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def get(self, section, key, default=None):
        """Get configuration value"""
        return self.config.get(section, {}).get(key, default)
    
    def set(self, section, key, value):
        """Set configuration value"""
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value
        self.save_config()
    
    def get_all(self):
        """Get all configuration"""
        return self.config