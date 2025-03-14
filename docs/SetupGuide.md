# Setup Guide

This guide explains how to set up the hardware and software for the Driver Fatigue Monitoring System.

## Hardware Setup

### Components Required:
- **Raspberry Pi 4 (4GB recommended)**
- **IR-enabled Camera Module:**  
  - Use the official Raspberry Pi NoIR Camera or a USB webcam with IR capability.
- **Buzzer/Alert Device:**  
  - A piezoelectric buzzer or speaker connected via GPIO.
- **(Optional) IMU Sensor:**  
  - For additional head movement data (e.g., MPU-6050).
- **Power Supply:**  
  - 12V-to-5V converter (or a powered USB hub if using a Pi).

### Assembly Instructions:
1. **Mount the Camera:**  
   - Position the IR camera so it has a clear, unobstructed view of the driver’s face.
   - Secure the camera using a mount or adhesive.
2. **Connect the Raspberry Pi:**  
   - Attach the camera to the Pi via the dedicated camera port (if using the Pi Camera) or a USB port (if using a USB webcam).
   - Connect the buzzer to one of the GPIO pins (refer to the Pi’s pinout diagram).
3. **Power Up:**  
   - Use a proper 5V power supply for the Raspberry Pi.
   - Ensure all components are securely connected and housed in an appropriate case if necessary.

## Software Setup

### Environment Setup:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Driver-Fatigue-Monitoring-System.git
   cd Driver-Fatigue-Monitoring-System
   
2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt