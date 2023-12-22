import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera, change it if you have multiple cameras

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # Define the codec (MP4V for MP4)
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))  # Output video filename, codec, FPS, and frame size

while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        print("Error: Failed to capture frame")
        break

    out.write(frame)  # Write the frame to the video file

    # Remove the preview window to not show the captured frame
    # cv2.imshow('Video Capture', frame)  # This line is removed

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break

# Release everything when the job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
