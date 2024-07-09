import cv2

# Load the video
video_path = '/Users/apple/Documents/Project/movie_dp.MP4'
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video")
    exit()

frame_count = 0

# Iterate through frames
while True:
    ret, frame = cap.read()

    # Check if frame is read successfully
    if not ret:
        break

    # Save frame as an image
    frame_filename = f"/Users/apple/Documents/Project/images/frame_{frame_count}.jpg"
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

# Release the capture object and close the window
cap.release()
cv2.destroyAllWindows()
