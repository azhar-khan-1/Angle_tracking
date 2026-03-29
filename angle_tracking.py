import cv2
import numpy as np

# ----------- FUNCTION: CALCULATE ANGLE -----------
def calculate_angle(A, B, C):
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)

    v1 = A - B
    v2 = C - B

    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    angle = np.degrees(np.arccos(cos_theta))
    return angle

# ----------- LOAD VIDEO -----------
video_path = "angle tracking.mp4"
cap = cv2.VideoCapture(video_path)

ret, first_frame = cap.read()

points = []

# ----------- MOUSE CLICK FUNCTION -----------
def select_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 3:
            points.append((x, y))

cv2.imshow("Select 3 Points: Hip, Knee, Ankle", first_frame)
cv2.setMouseCallback("Select 3 Points: Hip, Knee, Ankle", select_points)

# Wait until 3 points selected
while True:
    temp = first_frame.copy()
    for p in points:
        cv2.circle(temp, p, 5, (0, 255, 0), -1)

    cv2.imshow("Select 3 Points: Hip, Knee, Ankle", temp)
    if len(points) == 3:
        break
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

points = np.array(points, dtype=np.float32)

# ----------- VIDEO WRITER -----------
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, 30,
                      (first_frame.shape[1], first_frame.shape[0]))

# ----------- TRACKER -----------
tracker = cv2.calcOpticalFlowPyrLK

old_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
p0 = points.reshape(-1, 1, 2)

# ----------- PROCESS VIDEO -----------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None)

    good_new = p1[st == 1]
    good_old = p0[st == 1]

    if len(good_new) < 3:
        break

    p1_, p2_, p3_ = good_new[:3]

    # Draw lines
    cv2.line(frame, tuple(p1_.astype(int)), tuple(p2_.astype(int)), (255, 0, 255), 2)
    cv2.line(frame, tuple(p2_.astype(int)), tuple(p3_.astype(int)), (255, 0, 255), 2)

    # Calculate angles
    angle_knee = calculate_angle(p2_, p1_, p3_)
    angle_ankle = calculate_angle(p1_, p2_, p3_)
    angle_foot = calculate_angle(p2_, p3_, p1_)

    # Display text
    cv2.putText(frame, f"Knee: {angle_knee:.1f}",
                tuple(p1_.astype(int)), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 255), 2)

    cv2.putText(frame, f"Ankle: {angle_ankle:.1f}",
                tuple(p2_.astype(int)), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 255), 2)

    cv2.putText(frame, f"Foot: {angle_foot:.1f}",
                tuple(p3_.astype(int)), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 255), 2)

    # Draw points
    for p in [p1_, p2_, p3_]:
        cv2.circle(frame, tuple(p.astype(int)), 5, (255, 255, 255), -1)

    cv2.imshow("Tracking", frame)
    out.write(frame)

    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Processing Complete")
