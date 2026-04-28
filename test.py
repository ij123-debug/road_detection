from ultralytics import YOLO
import cv2

# load model
model = YOLO("best.pt")   # changed path (important)

# open video
cap = cv2.VideoCapture("road.mp4")

# get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# save output video
out = cv2.VideoWriter("output.avi",
                      cv2.VideoWriter_fourcc(*'XVID'),
                      fps,
                      (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # run detection
    results = model(frame)

    # draw boxes
    annotated_frame = results[0].plot()

    # save frame instead of showing
    out.write(annotated_frame)

cap.release()
out.release()

print("✅ Output saved as output.avi")