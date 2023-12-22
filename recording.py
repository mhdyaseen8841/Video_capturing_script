import cv2
import time
import os

# Create a new folder based on timestamp
timestamp = int(time.time())
folder_name = f"videos_{timestamp}"
os.makedirs(folder_name)

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera, change it if you have multiple cameras

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # Define the codec (MP4V for MP4)
out = None
segment_duration = 15  # Segment duration in seconds
start_time = time.time()

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        print("Error: Failed to capture frame")
        break

    if out is None or (time.time() - start_time) > segment_duration:
        # Release the previous writer
        if out is not None:
            out.release()

        # Create a new VideoWriter for the next segment
        start_time = time.time()
        segment_name = f"{folder_name}/output_{int(start_time)}.mp4"  # Unique segment name based on timestamp
        out = cv2.VideoWriter(segment_name, fourcc, 20.0, (640, 480))  # Output video filename, codec, FPS, and frame size

    out.write(frame)  # Write the frame to the video file

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break

# Release everything when the job is finished
cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()
