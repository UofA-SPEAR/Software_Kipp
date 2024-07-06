import cv2 as cv

cap = cv.VideoCapture(0)
image_counter = 1  # Initialize the counter

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv.imshow('Video', frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord(' '):  # Spacebar key
        image_filename = f"boat{image_counter}.jpg"
        cv.imwrite(image_filename, frame)
        print(f"Image captured and saved as {image_filename}.")
        image_counter += 1  # Increment the counter
    elif key == ord('q'):  # 'q' key to quit
        break

cap.release()
cv.destroyAllWindows()
