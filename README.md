

# 🎯 Real-Time Hand-Controlled LEDs  


## 📌 Project Overview  

This project detects hand gestures using **computer vision**, converts the recognized number to **binary**, and sends it to an **Arduino via SPI** to control **LED lights** in real time.  

## 📖 Table of Contents  
- [How It Works](#-how-it-works)  
- [Requirements](#-requirements)  
- [Setup and Usage](#-setup-and-usage)  
- [Notes & Troubleshooting](#-notes--troubleshooting)  

## ⚙️ How It Works  

1️⃣ **Hand Tracking** - Uses a webcam and **Mediapipe** to track hand gestures.  
2️⃣ **Number Recognition** - A trained model identifies the number formed by fingers.  
3️⃣ **Binary Conversion** - The number is converted into a **3-bit binary** format.  
4️⃣ **SPI Communication** - The data is sent from **Python to Arduino** using the **SPI protocol**.  
5️⃣ **LED Control** - The Arduino receives the data and turns **LEDs ON/OFF** accordingly.  

### 🔢 Binary LED Representation Example  

| Number | Binary | LED1 (Pin 13) | LED2 (Pin 12) | LED3 (Pin 11) |
|---------|--------|---------------|---------------|---------------|
| 0       | 000    | OFF           | OFF           | OFF           |
| 1       | 010    | OFF           | ON            | OFF           |
| 2       | 100    | ON            | OFF           | OFF           |
| 3       | 110    | ON            | ON            | OFF           |

## 🛠 Requirements  

### 🔹 Software  
- Python 3.8+  
- Arduino IDE  

### 🔹 Python Libraries  
```bash
pip install opencv-python mediapipe numpy pickle pyserial
```

### 🔹 Hardware  
- **Arduino UNO/Nano**  
- **3 LEDs** connected to **pins 11, 12, and 13**  
- **USB Camera** for real-time hand detection  

## 🚀 Setup and Usage  

### 1️⃣ Upload Arduino Code  
- Open the **Arduino IDE** and upload the provided sketch to your **Arduino board**.

### 2️⃣ Run Python Script  
```bash
python inference_classifier.py
```

### 3️⃣ Perform Hand Gestures  
- Place your hand in front of the camera.  
- The system will recognize the **number** and **light up the LEDs** based on its binary representation.  

## ❗ Notes & Troubleshooting  

- Ensure **Arduino is connected** to the correct **COM port** (Modify it in `inference_classifier.py`).  
- The camera should have **good lighting** to improve detection accuracy.  
- If the LEDs are **not responding**, check the **wiring** and **SPI settings**.  

---

### 📜 License  
This project is licensed under the **MIT License**.  

---

