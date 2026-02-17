# ✋ Real-Time Finger Counter

A real-time computer vision application that detects hands and counts raised fingers using MediaPipe and OpenCV.

---

## 📌 Project Overview

This project uses MediaPipe's Hand Landmarker model to detect 21 hand landmarks and applies coordinate comparison logic to determine how many fingers are raised.

The system works in real-time using a webcam and supports detection of both left and right hands.

---

## 🚀 Features

- Detects up to 2 hands
- Counts raised fingers for each hand
- Displays total finger count
- Real-time webcam processing

---

## 🧠 How It Works

1. Webcam captures live video
2. Frame is converted from BGR to RGB format
3. MediaPipe detects 21 hand landmarks
4. Finger tip coordinates are compared with joint coordinates
5. Finger count is calculated and displayed

---

## 🛠 Tech Stack

- Python
- OpenCV
- MediaPipe
- Computer Vision

---

## 📂 Project Structure
real-time-finger-counter/
│── main.py
│── hand_landmarker.task
│── README.md
---


## ▶️ How to Run
1️⃣ Clone the Repository
git clone https://github.com/your-username/real-time-finger-counter.git
cd real-time-finger-counter
2️⃣ Install Dependencies
pip install opencv-python mediapipe
3️⃣ Run the Project
python main.py
Press Q to exit the application.

## 📦 Requirements

- Python 3.8+
- Webcam
- OpenCV
- MediaPipe
---

## 🔮 Future Improvements

- Add gesture recognition (Thumbs Up, Peace, Fist)
- Add hand tracking ID
- Improve UI design
- Deploy as web app



