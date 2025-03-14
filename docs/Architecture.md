# System Architecture

## Overview
The system architecture for the Driver Fatigue Monitoring System comprises hardware components and software modules that work together in a real-time pipeline. The key elements include an IR-enabled camera, a Raspberry Pi 4 as the processing unit, and an alert system

## Architecture Diagram
*(Insert your diagram image here using Markdown syntax)*

## Hardware Components
- **Camera Module:** 
  - IR-enabled camera (e.g., Raspberry Pi NoIR Camera) for capturing the driver’s face in all lighting conditions
- **Processing Unit:** 
  - Raspberry Pi 4, running a Linux OS and handling all image processing and machine learning tasks
- **Alert Mechanism:**  
  - Buzzer, LED, and/or vibration motor for issuing alerts when drowsiness is detected
- **Optional Sensors:**  
  - IMU sensors (accelerometer/gyroscope) to provide additional head movement data

## Software Modules
- **Camera Interface:**  
  - Captures video frames from the camera using OpenCV
- **Face & Landmark Detection:**  
  - Uses dlib and OpenCV to detect faces and extract facial landmarks
- **Feature Extraction & Algorithm Processing:**  
  - Computes the Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR)
  - Estimates head pose using the solvePnP function
- **Drowsiness Evaluation:**  
  - Combines the EAR, MAR, and head pose data to decide if the driver is drowsy
- **Alert and Logging:**  
  - Triggers alerts (visual, audio, etc.) and logs events for further analysis

## Data Flow
1. **Image Acquisition:** The camera continuously captures frames
2. **Processing:** Each frame is converted to grayscale and processed to detect the face
3. **Feature Extraction:** Landmarks are extracted, and EAR, MAR, and head pose are computed
4. **Decision:** If thresholds are crossed, an alert is triggered
5. **Output:** Alerts are displayed on-screen and optionally logged for future review

## Link to Documentation on Canva
[SomnoCam Canva Doc](https://www.canva.com/design/DAGhVM_YV_U/DUiCkND-jsdqbEHmV9HLlg/edit?utm_content=DAGhVM_YV_U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

leave a comment if you have any suggestions
