# Manual Marker-Based Angle Calculation

> A biomechanics-based approach to compute joint angles using manual annotation for high-accuracy motion analysis.

---

##  Overview
This project demonstrates how joint angles (or segment angles) can be calculated from a video using **manual marker placement**.  
Instead of automated pose estimation, specific anatomical landmarks are manually marked frame-by-frame to ensure accuracy and control.

---

##  Objective
To calculate angles between body segments using manually selected points from video frames.

---

##  Methodology

### 1. Video Input
A motion video (e.g., athlete movement, gait, or exercise) is used.

### 2. Frame Extraction
The video is divided into individual frames.

### 3. Manual Marker Placement
Key points (e.g., shoulder, elbow, hip, knee) are manually selected on each frame.

### 4. Coordinate Extraction
The (x, y) coordinates of each marker are recorded.

### 5. Angle Calculation
Angles are calculated using vector mathematics.

Formula used:
cos(θ) = (BA · BC) / (|BA| |BC|)  
θ = cos⁻¹(...)

---

## Results
- Angle values calculated for each frame  
- Frame-by-frame motion analysis  
- Accurate joint angle estimation using manual annotation  

---
##  Demo

This video demonstrates the process of manually marking anatomical points and calculating joint angles frame-by-frame.

▶️ **Watch Demo Video:**  
[View on Google Drive](https://drive.google.com/file/d/1Rprh8NsqBaEbCnW0t9gnPsRudWXPirWM/view?usp=drive_link)


---

##  Advantages
- High accuracy (no model-based errors)  
- Full control over marker placement  
- Useful for validation of AI-based pose estimation systems  

---

##  Limitations
- Time-consuming (manual process)  
- Prone to human error  
- Not scalable for large datasets  

---

##  Future Improvements
- Automate marker detection using computer vision  
- Integrate pose estimation models (e.g., OpenPose, MediaPipe)  
- Real-time angle tracking system  
- GUI for easy annotation  

---

## Tools Used
- Python  
- NumPy  
- OpenCV (optional)  

---

##  Applications
- Sports biomechanics  
- Athlete performance analysis  
- Rehabilitation and physiotherapy  
- Motion tracking research  

---

##  Author
**Azhar Khan**  
M.Tech Biomedical Engineering, IIT Indore  
