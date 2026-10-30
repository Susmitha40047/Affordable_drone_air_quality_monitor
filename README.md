# Affordable Drone Air Quality Monitoring Simulator

This project is a complete software prototype of an affordable drone-based air quality monitoring system. It simulates drone movement, GPS coordinates, air-quality readings, alerts, and mission logging through a Flask web application.

## Features

- Simulated drone mission with live GPS path
- Generated PM2.5, PM10, CO2, gas index, temperature, and humidity values
- Web dashboard with live cards, charts, and map
- Alert detection for high pollution zones
- Automatic CSV mission log creation

## Project Structure

```text
.
|-- app.py
|-- simulator.py
|-- requirements.txt
|-- README.md
|-- data/
|   `-- air_quality_data.csv
|-- static/
|   |-- app.js
|   `-- styles.css
`-- templates/
    `-- index.html
```

## How To Run

1. Create a virtual environment:

```powershell
python -m venv .venv
```

2. Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Start the application:

```powershell
python app.py
```

5. Open the browser at:

```text
http://127.0.0.1:5000
```

## Step-By-Step Simulation Flow

1. Press `Start Mission`.
2. The backend starts the mission thread.
3. Every second, a new route point is generated.
4. The simulator creates corresponding air-quality readings.
5. The data is added to the dashboard and saved to `data/air_quality_data.csv`.
6. Alerts appear automatically when PM2.5 or CO2 crosses a threshold.
7. Press `Pause Mission` to stop generation.
8. Press `Reset Mission` to clear history and restart from the first point.

## Demo Explanation

When presenting, explain the software in this order:

1. The drone route is simulated as a mission path on the map.
2. Each point acts like a sensor capture event from a drone payload.
3. The dashboard shows live environmental conditions.
4. Alerts help identify high-pollution zones.
5. The CSV file represents the mission data for future analysis.

## Future Hardware Upgrade Path

This prototype can later be connected to:

- ESP32 sensor node
- PMS5003 particulate sensor
- CO2 sensor
- GPS module
- Pixhawk flight controller
- Real telemetry link
