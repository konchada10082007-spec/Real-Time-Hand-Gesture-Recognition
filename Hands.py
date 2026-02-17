import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# ️ Load Hand Landmarker Model


base_options = python.BaseOptions(
    model_asset_path='hand_landmarker.task'
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2
)

hand_landmarker = vision.HandLandmarker.create_from_options(options)


#  Open Camera


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Camera opened")


#  Start Camera Loop


while True:
    success, frame = cap.read()
    if not success:
        break

    total_fingers_all = 0

    # Convert BGR → RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert to MediaPipe Image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    # Detect hands
    result = hand_landmarker.detect(mp_image)

    if result.hand_landmarks:

        for idx, hand_landmarks in enumerate(result.hand_landmarks):

            landmarks = hand_landmarks
            fingers = []

            handedness = result.handedness[idx][0].category_name

            
            # Thumb(Different for Left & Right)
            

            if handedness == "Right":
                if landmarks[4].x > landmarks[3].x:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:  # Left hand
                if landmarks[4].x < landmarks[3].x:
                    fingers.append(1)
                else:
                    fingers.append(0)

           
            # OTHER FINGERS
            

            # Index
            if landmarks[8].y < landmarks[6].y:
                fingers.append(1)
            else:
                fingers.append(0)

            # Middle
            if landmarks[12].y < landmarks[10].y:
                fingers.append(1)
            else:
                fingers.append(0)

            # Ring
            if landmarks[16].y < landmarks[14].y:
                fingers.append(1)
            else:
                fingers.append(0)

            # Pinky
            if landmarks[20].y < landmarks[18].y:
                fingers.append(1)
            else:
                fingers.append(0)

            total_fingers = sum(fingers)
            total_fingers_all += total_fingers

            
            # Draw Landmarks
            

            h, w, _ = frame.shape

            for point in landmarks:
                cx = int(point.x * w)
                cy = int(point.y * h)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

            
            # Display Hand Count
            

            cv2.putText(frame,
                        f"{handedness} Hand: {total_fingers}",
                        (20, 70 + idx * 60),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255, 0, 0),
                        2)

       
        # Display Total Count
     

        cv2.putText(frame,
                    f"Total Fingers: {total_fingers_all}",
                    (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2)

    cv2.imshow("Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
