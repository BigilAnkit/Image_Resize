import cv2
import os

# Load the image
img = cv2.imread("id.png", cv2.IMREAD_COLOR)

# Resize the image
resized_img = cv2.resize(img, (210, 310))

# Specify the output directory
output_directory = r"E:\Download2"

# Save the resized image
output_path = os.path.join(output_directory, "resized_id.png")
cv2.imwrite(output_path, resized_img)

# Display the resized image
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
