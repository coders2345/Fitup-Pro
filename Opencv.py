import cv2

# Capture video from webcam
cap = cv2.VideoCapture(1)

# Define aspect ratio and height threshold for pushup detection
aspect_ratio = 0.5
height_threshold = 50

# Loop through frames of video
while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply threshold to create binary image
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through contours
    for contour in contours:
        # Compute the aspect ratio of the contour
        x, y, w, h = cv2.boundingRect(contour)
        contour_aspect_ratio = w / h

        # Filter out contours that are not roughly rectangular or don't have the correct aspect ratio
        if contour_aspect_ratio > aspect_ratio - 0.2 and contour_aspect_ratio < aspect_ratio + 0.2 and h > height_threshold:
            # Draw a rectangle around the contour
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
