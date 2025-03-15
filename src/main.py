import cv2
import dlib
import numpy as np
import imutils
from imutils import face_utils
import math

def eye_aspect_ratio(eye):
    a = np.linalg.norm(eye[1] - eye[5])
    b = np.linalg.norm(eye[2] - eye[4])
    c = np.linalg.norm(eye[0] - eye[3])
    return (a + b) / (2.0 * c)

def mouth_aspect_ratio(mouth):
    a = np.linalg.norm(mouth[3] - mouth[7])
    b = np.linalg.norm(mouth[2] - mouth[6])
    c = np.linalg.norm(mouth[0] - mouth[4])
    return (a + b) / (2.0 * c)

def get_head_pose(landmarks, frame, model_points):
    image_points = np.array([
        landmarks[30],  # Nose tip
        landmarks[8],   # Chin
        landmarks[36],  # Left eye, left corner
        landmarks[45],  # Right eye, right corner
        landmarks[48],  # Left mouth corner
        landmarks[54]   # Right mouth corner
    ], dtype="double")

    height, width = frame.shape[:2]
    focal_length = width
    center = (width // 2, height // 2)
    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]
    ], dtype="double")
    dist_coefficients = np.zeros((4, 1))

    success, rotation_vector, translation_vector = cv2.solvePnP(
        model_points, image_points, camera_matrix, dist_coefficients)

    (nose_end_point2D, _) = cv2.projectPoints(
        np.array([(0, 0, 1000.0)]),
        rotation_vector, translation_vector, camera_matrix, dist_coefficients)
    return image_points, rotation_vector, translation_vector, nose_end_point2D

def rotationMatrixToEulerAngles(R):
    sy = math.sqrt(R[0, 0] ** 2 + R[1, 0] ** 2)
    singular = sy < 1e-6
    if not singular:
        roll = math.atan2(R[2, 1], R[2, 2])
        pitch = math.atan2(-R[2, 0], sy)
        yaw = math.atan2(R[1, 0], R[0, 0])
    else:
        roll = math.atan2(-R[1, 2], R[1, 1])
        pitch = math.atan2(-R[2, 0], sy)
        yaw = 0
    return np.array([yaw, pitch, roll])

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

model_points = np.array([
    (0.0, 0.0, 0.0),             # Nose tip
    (0.0, -330.0, -65.0),         # Chin
    (-225.0, 170.0, -135.0),      # Left eye, left corner
    (225.0, 170.0, -135.0),       # Right eye, right corner
    (-150.0, -150.0, -125.0),     # Left mouth corner
    (150.0, -150.0, -125.0)       # Right mouth corner
])

EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.75
PITCH_THRESHOLD = -20  # Degrees: pitch below this suggests head nodding

frame = imutils.resize(frame, width=600)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

rects = detector(gray, 1)
for rect in rects:
    # Draw a bounding box around the face
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    landmarks = predictor(gray, rect)
    landmarks = face_utils.shape_to_np(landmarks)

    for (x_point, y_point) in landmarks:
        cv2.circle(frame, (x_point, y_point), 1, (0, 0, 255), -1)

    rightEye = landmarks[36:42]
    leftEye = landmarks[42:48]
    mouth = landmarks[60:68]

    ear_right = eye_aspect_ratio(rightEye)
    ear_left = eye_aspect_ratio(leftEye)
    ear = (ear_right + ear_left) / 2.0
    mar = mouth_aspect_ratio(mouth)

    cv2.putText(frame, f"EAR: {ear:.2f}", (x, y - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.putText(frame, f"MAR: {mar:.2f}", (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    image_points, rotation_vector, translation_vector, nose_end_point2D = get_head_pose(landmarks, frame, model_points)
    pt1 = (int(image_points[0][0]), int(image_points[0][1]))
    pt2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
    cv2.line(frame, pt1, pt2, (255, 0, 255), 2)

    rotation_mat, _ = cv2.Rodrigues(rotation_vector)
    euler_angles = rotationMatrixToEulerAngles(rotation_mat)
    yaw, pitch, roll = np.degrees(euler_angles)
    cv2.putText(frame, f"Yaw: {yaw:.1f}", (x, y + h + 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 2)
    cv2.putText(frame, f"Pitch: {pitch:.1f}", (x, y + h + 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 2)
    cv2.putText(frame, f"Roll: {roll:.1f}", (x, y + h + 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 2)


    drowsy_trigger = False
    alert_details = ""

    if ear < EAR_THRESHOLD:
        drowsy_trigger = True
        alert_details += f"EAR Faible: {ear:.2f} (seuil: {EAR_THRESHOLD})  "

    if mar > MAR_THRESHOLD:
        drowsy_trigger = True
        alert_details += f"MAR élevé: {mar:.2f} (seuil: {MAR_THRESHOLD})"

    if drowsy_trigger:
        status = "ALERTE: Somnolence detectee!"
        cv2.putText(frame, status, (x, y - 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(f"ALERTE: Conducteur fatigue! {alert_details}")
    else:
        status = "etat normal"
        cv2.putText(frame, status, (x, y - 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        print(f"La personne est alerte. EAR: {ear:.2f}, MAR: {mar:.2f}")

cv2.imshow("Output", frame)
output_filename = f"annotated_{image_path}"
cv2.imwrite(output_filename, frame)
print(f"Annotated image saved as '{output_filename}'")
cv2.waitKey(5000)
cv2.destroyAllWindows()


