# **Driver Drowsiness Detector**

## **Introduction**
**SomnoCam** or the **Driver Drowsiness Detector** is a **prototype project** aimed at exploring the feasibility of detecting driver drowsiness using computer vision and machine learning techniques

The system is designed to study how real-time monitoring can identify **signs of drowsiness** and issue alerts before accidents occur

### ❗ **Disclaimer**  
 **This is a research prototype and NOT a finalised commercial solution**  
The project is in its **development phase**, and further enhancements are needed for real-world deployment

### **Current Features**
  - Detects drowsiness from static images
  - Analyzes eye openness (EAR) and yawning (MAR) 
  - Head pose estimation using OpenCV

When drowsiness is detected, the system triggers **immediate alerts** (sound, vibration, or visual) to help the driver stay alert or take a break

🔗 **[Link to Project Documentation](https://www.canva.com/design/DAGhVM_YV_U/DUiCkND-jsdqbEHmV9HLlg/edit?utm_content=DAGhVM_YV_U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)**

## **Why is this Research Important**
- **18%** of fatal accidents are linked to driver fatigue
- **6,700 deaths** in 2021 in the U.S. were caused by drowsy driving
- After **20 hours without sleep**, a driver’s reaction time is as slow as someone with an illegal blood alcohol level

💡 **Traditional methods like drinking coffee or opening a window are ineffective**  
A data-driven, AI-based approach could provide more reliable drowsiness detection

## **Current Prototype**
This prototype consists of **image-based fatigue detection** using OpenCV and dlib
and it consists of **four main components**

### **Image Processing (No Real-Time Support Yet)**
- Static image input only (JPEG, PNG, etc)
- Detects drowsiness indicators in a single image

### **Detection Algorithms (Applied to Images)**
- **Facial landmark detection** (dlib 68-point model)
- **Eye Aspect Ratio (EAR):** Identifies closed eyes
- **Mouth Aspect Ratio (MAR):** Detects yawning
- **Head Pose Estimation:**  
- If the head tilts forward or sideways → Fatigue likely

## **Final Prototype Design**
The goal of this project is to develop a **fully functional driver drowsiness detection system** capable of **real-time drowsiness monitoring** in vehicles. 
This will involve **buying specialized hardware, optimizing algorithms, and adding new features**

### **Planned Features & Upgrades**
| Component | Current Status | Future Enhancements |
|-----------|---------------|---------------------|
| **Hardware** | No real hardware used yet, only image-based detection | Purchase and integrate **Raspberry Pi Camera** & **IR Camera** for real-time processing |
| **Video Stream Processing** | Works only on static images | Implement **real-time video stream analysis** for continuous fatigue monitoring |
| **Detection Algorithms** | Basic EAR, MAR, and Head Pose using OpenCV | Upgrade to **deep learning models (CNN, LSTM)** for **higher accuracy** |
| **AI & Machine Learning** | Rule-based thresholds for EAR/MAR | Train a **custom dataset** and use **gaze tracking** for improved detection |
| **Alert System** | No alerts implemented yet | Add **buzzer, LED warning system, or seat vibration motor** |
| **Hardware Performance** | Runs on standard PC / Raspberry Pi | Optimize performance for **low-latency processing** on **Jetson Nano** |
| **User Interface** | No UI | Create a **dashboard to display fatigue alerts** |
| **Mobile & Cloud Integration** | No mobile app or cloud features | Develop a **mobile app** for real-time notifications & **journalisation** |

**The final prototype will be a compact, AI-powered edge device capable of real-time driver monitoring and fatigue alerts**  
**This system could help improve road safety by preventing accidents caused by drowsiness**

### **Software Installation**
#### **Clone the GitHub Repository**
```bash
git clone https://github.com/SomnoCam/Driver-Fatigue-Monitoring-System.git
cd Driver-Fatigue-Monitoring-System
