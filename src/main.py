import os
import cv2
import dlib
import numpy as np
import imutils
from imutils import face_utils
import math

def eye_aspect_ratio(eye):
    """
    Compute the Eye Aspect Ratio (EAR)
    """
    vertical1 = np.linalg.norm(eye[1] - eye[5])
    vertical2 = np.linalg.norm(eye[2] - eye[4])
    horizontal = np.linalg.norm(eye[0] - eye[3])
    return (vertical1 + vertical2) / (2.0 * horizontal)

def mouth_aspect_ratio(mouth):
    """
    Compute the Mouth Aspect Ratio
    """
    vertical1 = np.linalg.norm(mouth[3] - mouth[7])
    vertical2 = np.linalg.norm(mouth[2] - mouth[6])
    horizontal = np.linalg.norm(mouth[0] - mouth[4])
    return (vertical1 + vertical2) / (2.0 * horizontal)

def get_head_pose(landmarks, frame, model_points):
    """
    Estimate head pose based on facial landmarks.
    """
    # Select key facial points for pose estimation
    image_points = np.array([
        landmarks[30],  # Nose tip
        landmarks[8],   # Chin
        landmarks[36],  # Left eye, left corner
        landmarks[45],  # Right eye, right corner
        landmarks[48],  # Left mouth corner
        landmarks[54]   # Right mouth corner
    ], dtype="double")

    height, width = frame.shape[:2]
    focal_length = width  # Approximation for focal length
    center = (width // 2, height // 2)
    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]
    ], dtype="double")
    dist_coefficients = np.zeros((4, 1))  # Assuming no lens distortion

    success, rotation_vector, translation_vector = cv2.solvePnP(
        model_points, image_points, camera_matrix, dist_coefficients
    )

    (nose_end_point2D, _) = cv2.projectPoints(
        np.array([(0, 0, 1000.0)]),
        rotation_vector, translation_vector, camera_matrix, dist_coefficients
    )
    return image_points, rotation_vector, translation_vector, nose_end_point2D

def rotation_matrix_to_euler_angles(r):
    """
    Convert rotation matrix to Euler angles
    """
    sy = math.sqrt(r[0, 0] ** 2 + r[1, 0] ** 2)
    singular = sy < 1e-6
    if not singular:
        roll = math.atan2(r[2, 1], r[2, 2])
        pitch = math.atan2(-r[2, 0], sy)
        yaw = math.atan2(r[1, 0], r[0, 0])
    else:
        roll = math.atan2(-r[1, 2], r[1, 1])
        pitch = math.atan2(-r[2, 0], sy)
        yaw = 0
    return np.array([yaw, pitch, roll])

def process_image(image_path):
    """
    Process image
    """
    # Initialising dlib face detector and shape predictor
    print("[INFO] Loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

    # 3D model for the head pose estimation
    model_points = np.array([
        (0.0, 0.0, 0.0),              # Nose tip
        (0.0, -330.0, -65.0),         # Chin
        (-225.0, 170.0, -135.0),      # Left eye, left corner
        (225.0, 170.0, -135.0),       # Right eye, right corner
        (-150.0, -150.0, -125.0),     # Left mouth corner
        (150.0, -150.0, -125.0)       # Right mouth corner
    ])

    # Drowsiness thresholds
    EAR_THRESHOLD = 0.25
    MAR_THRESHOLD = 0.75

    # Load and preprocess image
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"[ERROR] Could not load image '{image_path}'.")
        return
    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    print("[INFO] Detecting faces...")
    faces = detector(gray, 1)

    for face in faces:
        (x, y, w, h) = face_utils.rect_to_bb(face)
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Determine facial landmarks and convert them to NumPy array
        shape = predictor(gray, face)
        landmarks = face_utils.shape_to_np(shape)

        # Draw each facial landmark on the frame
        for (x_point, y_point) in landmarks:
            cv2.circle(frame, (x_point, y_point), 1, (0, 0, 255), -1)

        # Extract eye and mouth coordinates
        right_eye = landmarks[36:42]
        left_eye = landmarks[42:48]
        mouth = landmarks[60:68]

        # Compute aspect ratios
        ear_right = eye_aspect_ratio(right_eye)
        ear_left = eye_aspect_ratio(left_eye)
        ear = (ear_right + ear_left) / 2.0
        mar = mouth_aspect_ratio(mouth)

        # Overlay EAR and MAR on the image
        cv2.putText(frame, f"EAR: {ear:.2f}", (x, y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(frame, f"MAR: {mar:.2f}", (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Estimate head pose
        image_points, rotation_vector, translation_vector, nose_end_point2D = get_head_pose(landmarks, frame, model_points)
        pt1 = (int(image_points[0][0]), int(image_points[0][1]))
        pt2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
        cv2.line(frame, pt1, pt2, (255, 0, 255), 2)

        # Convert rotation vector to Euler angles
        rotation_mat, _ = cv2.Rodrigues(rotation_vector)
        euler_angles = rotation_matrix_to_euler_angles(rotation_mat)
        yaw, pitch, roll = np.degrees(euler_angles)
        cv2.putText(frame, f"Yaw: {yaw:.1f}", (x, y + h + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        cv2.putText(frame, f"Pitch: {pitch:.1f}", (x, y + h + 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        cv2.putText(frame, f"Roll: {roll:.1f}", (x, y + h + 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        # Check for signs of drowsiness
        alert_messages = []
        if ear < EAR_THRESHOLD:
            alert_messages.append(f"Low EAR: {ear:.2f} (Threshold: {EAR_THRESHOLD})")
        if mar > MAR_THRESHOLD:
            alert_messages.append(f"High MAR: {mar:.2f} (Threshold: {MAR_THRESHOLD})")

        if alert_messages:
            status = "ALERT: Drowsiness detected!"
            cv2.putText(frame, status, (x, y - 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print("[WARNING] Drowsiness detected!")
            for msg in alert_messages:
                print(f" - {msg}")
        else:
            status = "Status: Alert"
            cv2.putText(frame, status, (x, y - 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            print(f"[INFO] Person is alert. EAR: {ear:.2f}, MAR: {mar:.2f}")

    # Save and display result image
    output_filename = "result_images/result_" + os.path.basename(image_path)
    cv2.imwrite(output_filename, frame)
    print(f"[INFO] result image saved as '{output_filename}'")

    cv2.imshow("Output", frame)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

if __name__ == '__main__':

    input_image_path = 'images/test4.jpg'
    process_image(input_image_path)
