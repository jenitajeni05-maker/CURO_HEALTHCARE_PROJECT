🩺 CURO – Smart Emergency Healthcare Monitoring System

Project Overview
CURO is an AI-based healthcare monitoring prototype designed to **detect abnormal heart rate early and automatically alert nearby hospitals and family members**.
The goal of CURO is to reduce emergency response time and prevent sudden cardiac deaths by enabling **continuous health monitoring** using a smartwatch-like device.
This repository contains the **Python prototype simulation** of the CURO system workflow.

🚨 Problem Statement
Many heart attack deaths occur because:
* Symptoms are ignored or unnoticed
* Patients are alone during emergencies
* Hospitals are not informed in time
CURO solves this by providing **real-time monitoring + automatic emergency alerts**.

💡 Solution
CURO continuously monitors the user’s heart rate, detects abnormalities using a simple AI logic, and instantly sends alerts with **location + health data** to:
*  Nearby hospitals
*  Family members
*  
🏗️ System Architecture
![architecture png](https://github.com/user-attachments/assets/890e5a37-bb82-48cc-b3be-5753e40cc7eb)
### How the Prototype Works
### 1️.Baseline Learning
The system first learns the **normal heart rate range** of the user.
Example:
* Resting HR → 70 bpm
* Safe range → 60 – 100 bpm
This becomes the **personalized baseline**.
### 2. Continuous Monitoring
The smartwatch continuously reads heart rate data and sends it to the system.
In the prototype:
* Heartbeat values are simulated using Python.
### 3️.Health Data Storage
All collected heart rate data is stored for:
* Future medical analysis
* Emergency sharing with hospitals
### 4.Abnormality Detection (Core Logic)
The system checks if heart rate is:
* Too high (>120 bpm)
* Too low (<50 bpm)
If detected → **Emergency Trigger Activated**
This represents early detection of:
* Heart attack risk
* Arrhythmia
* Sudden cardiac arrest
### 5️.Location Identification 
The system fetches GPS coordinates of the patient so emergency services know **where to reach**.
### 6️.Emergency Alert System 
Once abnormal heart rate is detected:
Alert is sent via SMS to:
* Nearby hospital
* Family members
Alert message includes:
* Patient condition
* Heart rate value
* Live location

🧪 Prototype Simulation
This repo contains a **Python simulation** that demonstrates:
* Smartwatch data generation
* Abnormal heart rate detection
* Emergency alert trigger
Run the simulation:
```
curo_watch_simulation.py

```
### Future Scope
* Real smartwatch integration
* Real GPS tracking
* Hospital database integration
* Mobile app for patients & hospitals
* AI prediction of heart disease risk

Project Name: **CURO**

