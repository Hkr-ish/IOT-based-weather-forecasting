# IoT-Based Temperature Forecasting System (Simulation-Driven Approach)

## 📋 Introduction

This project demonstrates how to build a predictive machine learning system for forecasting room temperature **without physical IoT hardware**. Instead, it simulates sensor data, trains a regression model, and visualizes real-time predictions—all using Python and open-source libraries. This approach enables rapid prototyping and learning for students, hobbyists, and developers interested in IoT, time-series analysis, and ML, without the logistical overhead of actual devices.

---

## 🚩 Project Objective

- **Simulate** realistic time-series temperature data akin to IoT sensor readings.
- **Train and validate** a regression model to forecast future temperatures (e.g., 15 minutes ahead).
- **Visualize** actual and predicted temperatures on a live graph for instant feedback.
- **Build modular architecture** easily extendable to real IoT hardware in the future.

---

## 📝 Problem Statement

Modern smart environments benefit from proactive climate control. Predicting ambient temperature helps optimize HVAC systems for energy savings and comfort. However, the cost and complexity of setting up physical IoT hardware pose a barrier. This project provides a **hardware-free, simulation-based solution** to develop and test forecasting systems.

---

## 🏗️ Solution Overview & System Architecture

### Conceptual Framework

- **Synthetic Data Generation:** Simulate minute-by-minute temperature readings with natural fluctuations.
- **Model Training:** Use historical data to train a linear regression model for future predictions.
- **Real-Time Forecasting:** Simulate a data stream, generate predictions on-the-fly.
- **Live Visualization:** Plot actual vs. predicted temperatures using Matplotlib (optionally, Streamlit for web UI).

### Layered Architecture

1. **Simulation Layer:** Generates and saves synthetic temperature data (`temperature_data.csv`).
2. **Processing Layer:** Preprocesses data, engineers features, and trains a regression model (`temperature_model.pkl`).
3. **Prediction Layer:** Simulates data feed, uses model to predict future temperature.
4. **Presentation Layer:** Dynamically plots actual and predicted temperatures; optionally, display in Streamlit dashboard.

---

## 🛠️ Technology Stack

| Category          | Technology / Tool      | Purpose                                        |
| ----------------- | --------------------- | ---------------------------------------------- |
| Programming       | Python 3.x            | Core scripting and logic                       |
| Data Handling     | Pandas, NumPy         | Data manipulation, CSV, numerical operations   |
| Machine Learning  | Scikit-learn          | Model training and evaluation                  |
| Visualization     | Matplotlib            | Real-time graphs and plots                     |
| Dashboarding      | Streamlit (Optional)  | Interactive web UI                             |
| Model Persistence | Joblib                | Saving/loading trained models                  |
| IDE/Dev           | VS Code, Jupyter      | Development environment                        |

---

## ⚙️ How to Implement

### 1. Clone the Repository

```bash
git clone https://github.com/priyanshupaikra/IoT-Temperature-Forecasting.git
cd IoT-Temperature-Forecasting
```

### 2. Install Dependencies

```bash
pip install numpy pandas scikit-learn matplotlib joblib streamlit
```

### 3. Generate Synthetic Temperature Data

Create and run a script (e.g., `simulate_temperature.py`) to generate timestamped temperature data with realistic noise and cycles.

```python
# simulate_temperature.py
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

minutes = 2 * 24 * 60  # 2 days of minute-level data
timestamps = [datetime.now() + timedelta(minutes=i) for i in range(minutes)]
base_temp = 22 + 4 * np.sin(np.linspace(0, 4*np.pi, minutes))  # Diurnal cycle
noise = np.random.normal(0, 0.5, minutes)
temps = base_temp + noise

df = pd.DataFrame({'timestamp': timestamps, 'temperature': temps})
df.to_csv('temperature_data.csv', index=False)
```

### 4. Train the Regression Model

Create and run a script (e.g., `train_model.py`) to preprocess the data, engineer features, and train a Linear Regression model.

```python
# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from joblib import dump

df = pd.read_csv('temperature_data.csv')
window = 15
X, y = [], []
for i in range(window, len(df)-window):
    X.append(df['temperature'].iloc[i-window:i].values)
    y.append(df['temperature'].iloc[i+window])

import numpy as np
X = np.array(X)
y = np.array(y)

model = LinearRegression()
model.fit(X, y)
dump(model, 'temperature_model.pkl')

# Print metrics
y_pred = model.predict(X)
print("R2 Score:", r2_score(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))
```

### 5. Real-Time Prediction & Visualization

Create and run a script (e.g., `real_time_forecast.py`) to simulate live data feed and plot predictions.

```python
# real_time_forecast.py
import pandas as pd
import numpy as np
from joblib import load
import matplotlib.pyplot as plt

df = pd.read_csv('temperature_data.csv')
model = load('temperature_model.pkl')
window = 15

actuals, preds = [], []
plt.ion()
fig, ax = plt.subplots()
for i in range(window, len(df)-window):
    X_live = df['temperature'].iloc[i-window:i].values.reshape(1, -1)
    prediction = model.predict(X_live)[0]
    actual = df['temperature'].iloc[i+window]
    actuals.append(actual)
    preds.append(prediction)

    ax.clear()
    ax.plot(actuals, label='Actual')
    ax.plot(preds, label='Predicted')
    ax.legend()
    ax.set_title('Real-Time Temperature Forecasting')
    plt.pause(0.01)
plt.ioff()
plt.show()
```

#### Optional: Streamlit Dashboard

Create a more interactive UI using Streamlit.

```python
# streamlit_app.py
import streamlit as st
# ... (reuse code above to visualize in a Streamlit app)
```
Run with:
```bash
streamlit run streamlit_app.py
```

---

## 🎯 Expected Deliverables

- **temperature_data.csv:** Synthetic temperature dataset.
- **temperature_model.pkl:** Trained regression model.
- **Real-Time Visualization:** Live graph or dashboard comparing actual and predicted temperatures.
- **Performance Metrics:** R² score and Mean Squared Error (MSE) printed during training and optionally displayed in the dashboard.

---

## 🔮 Future Scope

- Integrate real IoT sensors (DHT11/DHT22, Arduino/ESP32, Raspberry Pi).
- Stream data to cloud platforms (Firebase, AWS IoT, ThingsBoard).
- Experiment with advanced models (Random Forest, Gradient Boosting, LSTM, Prophet).
- Add multi-sensor support (humidity, CO₂, pressure) for holistic monitoring.

---

## 📚 References

- [Scikit-learn Documentation](https://scikit-learn.org)
- [Pandas Documentation](https://pandas.pydata.org)
- [Matplotlib Documentation](https://matplotlib.org)
- [Streamlit Documentation](https://streamlit.io)
- [Overview of IoT Concepts](https://www.iotforall.com)

---

## 🏁 Conclusion

This project makes it easy to experiment with temperature prediction in smart environments—**no hardware required**. It provides a practical foundation for learning, prototyping, and scaling up to real-world IoT deployments.

---