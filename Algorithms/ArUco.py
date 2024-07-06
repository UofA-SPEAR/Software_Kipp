import cv2 as cv

# Initialize the webcam
cap = cv.VideoCapture(0)

while True:
    # Load the ArUco dictionary
    dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_100)


    # Create parameters for the ArUco detector
    parameters = cv.aruco.DetectorParameters()

    # Create an ArUco detector object
    detector = cv.aruco.ArucoDetector(dictionary, parameters)

    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame from webcam")
        break

    # Detect ArUco markers in the frame
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(frame)

    # Count the number of detected markers
    num_markers = len(markerIds) if markerIds is not None else 0

    # Draw detected markers on the frame
    if markerIds is not None:
        frame = cv.aruco.drawDetectedMarkers(frame, markerCorners, markerIds)

    # Display the frame
    cv.imshow("Webcam", frame)


    # Check for 'q' key to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()
