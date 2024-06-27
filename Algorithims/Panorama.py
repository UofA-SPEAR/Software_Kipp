import cv2
import glob
import math

# Read images
imagefiles = glob.glob("boat/*")
imagefiles.sort()

images = []
for filename in imagefiles:
    img = cv2.imread(filename)
    if img is not None:
        images.append(img)
num_images = len(images)

# Ensure there are images to stitch
if num_images == 0:
    print("No images found or images couldn't be read.")
else:
    # Create a stitcher object and stitch images
    stitcher = cv2.Stitcher_create()
    status, result = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        # Save the result to an image file
        cv2.imwrite('stitched_image.png', result)
        print("Stitched image saved as 'stitched_image.png'")
    else:
        print(f"Error during stitching: {status}")
