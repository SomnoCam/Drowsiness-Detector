# **Driver Drowsiness Detector**

## **Introduction**
**SomnoCam** or the **Driver Drowsiness Detector** is a **prototype project** aimed at exploring the feasibility of detecting driver drowsiness using computer vision and machine learning techniques
The system is designed to study how real-time monitoring can identify **signs of drowsiness** and issue alerts before accidents occur

### ❗ **Disclaimer**  
 **This is a research prototype and NOT a finalised commercial solution**  
The project is in its **development phase**, and further enhancements are needed for real-world deployment

### **Current Features**
The system detects:
- **eye closure**
- **yawning**
- **Abnormal head tilt**  

When drowsiness is detected, the system triggers **immediate alerts** (sound, vibration, or visual) to help the driver stay alert or take a break

🔗 **[Link to Project Documentation](https://www.canva.com/design/DAGhVM_YV_U/DUiCkND-jsdqbEHmV9HLlg/edit?utm_content=DAGhVM_YV_U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)**

## **Why is this Research Important**
- **18%** of fatal accidents are linked to driver fatigue
- **6,700 deaths** in 2021 in the U.S. were caused by drowsy driving
- After **20 hours without sleep**, a driver’s reaction time is as slow as someone with an illegal blood alcohol level

💡 **Traditional methods like drinking coffee or opening a window are ineffective**  
A data-driven, AI-based approach could provide more reliable drowsiness detection

## **System Architecture**
The prototype consists of **four main components**:

### **Infrared (IR) Camera**
- Captures real-time video of the driver’s face
- Works **both day and night**
- **Compatible with glasses** (minimizing reflection issues)

### **Edge AI Processing Unit**
- Runs real-time Drowsiness detection algorithms
- Compatible with:
  - **Raspberry Pi 4**
  - **Google Coral AI Accelerator**
- **Advantages:**
  - No Internet connection required
  - Ultra-fast processing

### **Detection Algorithms**
- **Facial landmark detection** using OpenCV and deep learning
- **Eye Aspect Ratio (EAR):** Detects prolonged eye closure
- **Mouth Aspect Ratio (MAR):** Detects yawning
- **Head Pose Analysis:**  
  - If the head tilts forward or sideways → Increased fatigue risk

### **Alert System**
- **Sound alerts** (buzzer or voice prompt)
- **Seat or steering wheel vibration**
  
## **Installation**
### **Hardware Requirements**
- **Raspberry Pi 4**
- **IR Camera)**
- **Buzzer and/or LED for alerts**

### **Software Installation**
#### **Clone the GitHub Repository**
```bash
git clone https://github.com/SomnoCam/Driver-Fatigue-Monitoring-System.git
cd Driver-Fatigue-Monitoring-System
