# Affordable Drone Air Quality Monitoring System

## Final Project Document

### Team Details

- **Team Number:** 5
- **1. 2310040047 - G. S. Susmitha**
- **2. 2310040081 - S. Vaishnavi**
- **3. 2310040061 - P. Shruthi**
- **4. 2310040034 - L. Archana**

### Project Title

**Affordable Drone Air Quality Monitoring System**

### Abstract

This project presents a software-based implementation of an affordable drone air quality monitoring system. The aim of the project is to simulate how a drone can be used to collect air pollution data from different geographic locations and display the information in real time through a web dashboard. Conventional air quality monitoring stations are costly and fixed to a particular location, which limits their spatial coverage. To overcome this limitation, the proposed system uses the concept of a mobile drone platform with environmental sensing capability.

In this project, the hardware behavior is represented through software simulation because of time limitations for full physical implementation. The developed prototype simulates drone movement, GPS coordinates, and environmental readings such as PM2.5, PM10, CO2, gas index, temperature, and humidity. The data is processed by a backend application and displayed on a live dashboard containing route mapping, trend charts, and pollution alerts. The complete mission data is also saved in CSV format for later analysis.

This system demonstrates the overall working principle of a drone-based air quality monitoring platform and provides a strong foundation for future real-time integration with actual drone hardware, sensors, and wireless communication modules.

### Keywords

Drone, Air Quality Monitoring, Flask, Simulation, GPS Tracking, Dashboard, Pollution Detection, IoT

## 1. Introduction

Air pollution is one of the major environmental issues affecting public health and ecological balance. Monitoring air quality is important in urban areas, industrial regions, traffic zones, and restricted places where pollution levels may vary significantly. Traditional air quality monitoring systems are generally expensive, stationary, and limited in coverage.

A drone-based monitoring system can solve this problem by moving across multiple locations and collecting data dynamically. Due to the short project timeline, this work focuses on the software implementation of the complete system behavior. The developed simulation visually represents how a real drone-based air quality monitoring system would operate in practical use.

## 2. Problem Statement

Fixed air quality monitoring stations are expensive and cannot efficiently monitor multiple locations in a short period of time. There is a need for a low-cost and portable system that can collect environmental data from different areas and present the information clearly for analysis.

## 3. Objectives

- To design a software prototype of an affordable drone-based air quality monitoring system
- To simulate drone movement over a predefined route using GPS coordinates
- To simulate air quality parameters such as PM2.5, PM10, CO2, gas index, temperature, and humidity
- To build a live web dashboard for data visualization
- To generate alerts when pollution values exceed safe levels
- To store mission data in CSV format for future analysis

## 4. Proposed System

The proposed system is a software simulation of a drone carrying air quality sensors. The drone travels across a set of predefined mission points. At each point, simulated sensor readings are generated and processed. The data is then displayed on a web dashboard and stored in a file.

### Main Functional Parts

- Drone path simulation
- Sensor data simulation
- Backend data processing
- Dashboard visualization
- Alert generation
- Mission data logging

## 5. System Architecture

```text
[Drone Route Simulator]
          |
          v
[Sensor Data Generator]
          |
          v
[Flask Backend]
     |           |
     v           v
[CSV Log]   [Web Dashboard]
                  |
                  v
         [Map + Charts + Alerts]
```

## 6. Software Tools Used

- **Programming Language:** Python
- **Framework:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Charts:** Chart.js
- **Map Visualization:** Leaflet.js
- **Data Storage:** CSV
- **IDE/Editor:** Visual Studio Code or any Python-supported editor

## 7. Implementation Details

### 7.1 Backend

The backend is developed using Flask. It manages the mission state, controls the simulation, and provides API endpoints for the dashboard. The application performs the following tasks:

- Starts the virtual mission
- Stops the mission
- Resets the mission
- Sends current and historical sensor data to the dashboard
- Stores readings in CSV format

### 7.2 Drone Simulation

The drone route is generated as a list of GPS coordinates around a central location. The simulated drone moves through these points continuously. Each point represents one monitoring event.

### 7.3 Sensor Simulation

At every route point, the system generates realistic values for:

- PM2.5
- PM10
- CO2
- Gas Index
- Temperature
- Humidity
- Altitude
- Speed

Random variation and hotspot logic are included to simulate changing environmental conditions and pollution peaks.

### 7.4 Dashboard

The dashboard provides:

- Live metric cards
- Route map with drone position
- Pollution trend chart
- Environmental trend chart
- Alert panel for higher pollution readings

## 8. Working Procedure

1. The user opens the dashboard in the browser.
2. The user clicks the **Start Mission** button.
3. The backend starts generating route points and sensor values every second.
4. The dashboard fetches the live data from the backend.
5. The map updates the drone position.
6. Charts update pollution and environmental trends.
7. Alerts appear when PM2.5 or CO2 exceeds the threshold.
8. All readings are saved to a CSV file.
9. The mission can be paused or reset at any time.

## 9. Modules Developed

### Module 1: Flask Application

- Handles routing and API endpoints
- Connects frontend and simulator

### Module 2: Mission Simulator

- Generates route points
- Simulates real-time mission execution

### Module 3: Sensor Data Generator

- Creates realistic pollution and environmental values
- Marks unsafe conditions

### Module 4: Dashboard Interface

- Displays live cards, charts, and route map

### Module 5: Data Logger

- Stores all mission readings in CSV format

## 10. Output Screens Expected

- Home dashboard with project title
- Mission control buttons
- Live drone route on map
- PM2.5, PM10, CO2, temperature, humidity cards
- Line charts for pollution trends
- Alert panel for pollution hotspots

## 11. Advantages

- Low-cost concept compared to fixed monitoring stations
- Covers multiple locations
- Provides live visualization
- Easy to upgrade with real hardware later
- Useful for smart city and academic applications

## 12. Applications

- Urban pollution monitoring
- Industrial area surveillance
- Traffic zone analysis
- Environmental research
- Campus demonstration projects

## 13. Limitations

- Current project is a software simulation only
- No direct hardware sensor integration in the present version
- Real drone calibration and flight constraints are not included

## 14. Future Scope

- Integrate with real drone hardware
- Add ESP32-based sensor node
- Use actual PM and gas sensors
- Add autonomous waypoint missions using Pixhawk
- Upload data to cloud dashboard
- Build mobile app support

## 15. Conclusion

The project successfully demonstrates the complete working model of an affordable drone-based air quality monitoring system through software simulation. It shows how a drone can move across different locations, collect air quality data, and display the results in real time using a dashboard. The system also stores the collected data for analysis and generates alerts when pollution levels rise.

Although the present implementation is software-based, it effectively represents the overall concept and workflow of a practical drone monitoring system. This project can be extended into a full hardware solution in the future and serves as a useful academic prototype for environmental monitoring applications.

## 16. References

1. Flask Official Documentation
2. Chart.js Documentation
3. Leaflet.js Documentation
4. General concepts of air pollution monitoring and drone-based sensing systems
