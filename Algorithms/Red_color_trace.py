import cv2
import numpy as np

# Capture video from the camera
cap = cv2.VideoCapture(0)

# Define the range for bright red color in HSV
lower_red_1 = np.array([0, 120, 70])
upper_red_1 = np.array([10, 255, 255])
lower_red_2 = np.array([170, 120, 70])
upper_red_2 = np.array([180, 255, 255])

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a binary mask where red colors are white
    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # List to store the x-coordinates of detected red lights
    x_coords = []

    # Process each contour
    for contour in contours:
        # Calculate the center of the contour
        M = cv2.moments(contour)
        if M['m00'] > 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            # Add the x-coordinate to the list
            x_coords.append(cx)
            # Draw the center of the contour
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    # Calculate the average x value if any x-coordinates were detected
    if x_coords:
        avg_x = int(sum(x_coords) / len(x_coords))
        # Draw a vertical line at the average x-coordinate
        cv2.line(frame, (avg_x, 0), (avg_x, frame.shape[0]), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
