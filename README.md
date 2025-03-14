# Driver Fatigue Monitoring System

## Overview
The Driver Fatigue Monitoring System is a real-time solution designed to detect driver drowsiness using computer vision and machine learning. Running on a Raspberry Pi 4 with an IR-enabled camera and written in Python, the system calculates the Eye Aspect Ratio (EAR), Mouth Aspect Ratio (MAR), and estimates head pose to determine if the driver is drowsy. If fatigue is detected, it triggers immediate alerts (visual, audio, or tactile) to help prevent accidents.

## Features
- Real-time face and landmark detection using OpenCV and dlib.
- Calculation of EAR for monitoring eye closure.
- Calculation of MAR for detecting yawning.
- Head pose estimation to detect head nodding.
- Edge computing on a Raspberry Pi, ensuring low-latency operation.
- Modular design for easy future upgrades and integration.

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Driver-Fatigue-Monitoring-System.git
   cd Driver-Fatigue-Monitoring-System
