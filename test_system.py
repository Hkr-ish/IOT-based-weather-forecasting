import requests
import time
import sys

def test_system():
    """Test the IoT temperature forecasting system"""
    base_url = 'http://localhost:5000/api'
    
    print("Testing IoT Temperature Forecasting System...")
    print("=" * 50)
    
    # Test 1: Current temperature
    print("Test 1: Current Temperature API")
    try:
        response = requests.get(f'{base_url}/temperature/current')
        if response.status_code == 200:
            data = response.json()
            print(f"  Status: PASS")
            print(f"  Temperature: {data['temperature']}°C")
            print(f"  Time: {data['timestamp']}")
        else:
            print(f"  Status: FAIL - HTTP {response.status_code}")
    except Exception as e:
        print(f"  Status: FAIL - {str(e)}")
    
    print()
    
    # Test 2: Temperature history
    print("Test 2: Temperature History API")
    try:
        response = requests.get(f'{base_url}/temperature/history?hours=24')
        if response.status_code == 200:
            data = response.json()
            print(f"  Status: PASS")
            print(f"  Data points: {len(data)}")
            if len(data) > 0:
                print(f"  Latest temp: {data[-1]['temperature']}°C")
        else:
            print(f"  Status: FAIL - HTTP {response.status_code}")
    except Exception as e:
        print(f"  Status: FAIL - {str(e)}")
    
    print()
    
    # Test 3: Temperature forecast
    print("Test 3: Temperature Forecast API")
    try:
        response = requests.get(f'{base_url}/temperature/forecast?hours=24')
        if response.status_code == 200:
            data = response.json()
            print(f"  Status: PASS")
            print(f"  Forecast points: {len(data)}")
            if len(data) > 0:
                print(f"  Next temp: {data[0]['temperature']}°C")
        else:
            print(f"  Status: FAIL - HTTP {response.status_code}")
    except Exception as e:
        print(f"  Status: FAIL - {str(e)}")
    
    print()
    
    # Test 4: System status
    print("Test 4: System Status API")
    try:
        response = requests.get(f'{base_url}/status')
        if response.status_code == 200:
            data = response.json()
            print(f"  Status: PASS")
            print(f"  System status: {data['system_status']}")
            print(f"  Database status: {data['database']['status']}")
        else:
            print(f"  Status: FAIL - HTTP {response.status_code}")
    except Exception as e:
        print(f"  Status: FAIL - {str(e)}")
    
    print()
    
    # Test 5: Settings
    print("Test 5: Settings API")
    try:
        # Get current settings
        response = requests.get(f'{base_url}/temperature/settings')
        if response.status_code == 200:
            data = response.json()
            print(f"  Status: PASS")
            print(f"  Base temp: {data['base_temperature']}°C")
            print(f"  Amplitude: {data['amplitude']}°C")
        else:
            print(f"  Status: FAIL - HTTP {response.status_code}")
    except Exception as e:
        print(f"  Status: FAIL - {str(e)}")
    
    print()
    print("=" * 50)
    print("Testing complete!")

if __name__ == '__main__':
    test_system()