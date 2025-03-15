# **Algorithm Details**

This document provides an in-depth explanation of the four key algorithms used in the **Driver Fatigue Monitoring System (SFC)**:
- **Eye Aspect Ratio (EAR)**
- **Mouth Aspect Ratio (MAR)**
- **Head Pose Estimation**
- **Rotation Matrix to Euler Angles Conversion**

Each section includes:
- **Objective** (What the algorithm does)
- **Mathematical Formula**
- **Step-by-step breakdown**
- **Visualization**
- **Pseudocode Implementation**

## **Eye Aspect Ratio (EAR)**
### **Objective**
The **Eye Aspect Ratio (EAR)** measures **eye openness** to detect prolonged eye closure, which is a strong indicator of drowsiness

### **Mathematical Formula**

$$
EAR = \frac{\|P2 - P6\| + \|P3 - P5\|}{2 \times \|P1 - P4\|}
$$

Where:
- \( P1 \) and \( P4 \) are the left and right corners of the eye (horizontal distance)
- \( P2, P3, P5, P6 \) are vertical points defining the top and bottom eyelid

### **Step-by-Step Breakdown**
1. Compute the **vertical distance** between **P2 and P6**
2. Compute the **vertical distance** between **P3 and P5**
3. Compute the **horizontal distance** between **P1 and P4**
4. Apply the EAR formula.
5. If **EAR < 0.17** for more than 1 second → **Drowsiness detected**

## Mouth Aspect Ratio (MAR)

### **Objective**

The **Mouth Aspect Ratio (MAR)** detects excessive **mouth opening**, which is an indicator of **yawning** (a common fatigue sign).

### **Mathematical Formula**
$$
MAR = \frac{\|P3 - P7\| + \|P2 - P6\|}{2 \times \|P0 - P4\|}
$$
Where:

-   P0 and P4 are the corners of the mouth (horizontal)
-   P2, P3, P6, P7 define the upper and lower lips

### **Step-by-Step Breakdown**

1.  Compute the **vertical distance** between **P3 and P7**
2.  Compute the **vertical distance** between **P2 and P6**
3.  Compute the **horizontal distance** between **P0 and P4**
4.  Apply the MAR formula.
5.  If **MAR > 0.5** → **Yawning detected**
## Head Pose Estimation

### **Objective**

The **Head Pose Estimation** algorithm determines the orientation of the driver’s head using **Yaw, Pitch, and Roll** angles

-   **Yaw:** Left/right head rotation (distraction)
-   **Pitch:** Up/down head tilt (fatigue detection)
-   **Roll:** Sideways head tilt (loss of muscle control)

### **Methodology**

-   Select **six key facial landmarks**
-   Use **solvePnP** (OpenCV) to compute **3D head orientation**

### **Mathematical Model**

1.  Define **2D image points** from facial landmarks:
    -   Nose tip
    -   Chin
    -   Left/right eye corners
    -   Left/right mouth corners
2.  Define **3D model points** (generic face structure)
3.  Compute **camera calibration matrix**
4.  Apply **solvePnP** to find **rotation vector** and **translation vector**
5.  Convert rotation data into **Euler angles**

## **Rotation Matrix to Euler Angles**

### **Objective**

Convert the **rotation matrix** from `solvePnP` into **Euler angles** (Yaw, Pitch, Roll).

### **Mathematical Model**

1.  Compute `sy` to check if the rotation matrix is in a **singular state**
2.  **If not singular**, compute **roll, pitch, and yaw** using `atan2`
3.  **If singular**, apply an alternative formula and set yaw to 0

## ** Next Steps**

-   Tune **EAR and MAR thresholds** for better real-world accuracy
-   Improve **head pose estimation** with **gaze tracking**
-   Test deep learning models to complement classical methods

