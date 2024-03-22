import cv2

# Read the original image
original_image = cv2.imread(r"C:\Users\pedda\OneDrive\Desktop\open cv\1.jpg")

# Read the watermark image (must be a transparent PNG)
watermark_image = cv2.imread(r"C:\Users\pedda\OneDrive\Desktop\open cv\transparent-logo.webp", cv2.IMREAD_UNCHANGED)

# Get the dimensions of the watermark image
(watermark_height, watermark_width, _) = watermark_image.shape

# Define the position where you want to place the watermark
# For example, you can place it in the bottom right corner
start_y = original_image.shape[0] - watermark_height - 10  # 10 pixels margin
start_x = original_image.shape[1] - watermark_width - 10   # 10 pixels margin

# Get the region of interest (ROI) in the original image
roi = original_image[start_y:start_y + watermark_height, start_x:start_x + watermark_width]

# Resize the watermark image to match the dimensions of the ROI
watermark_image_resized = cv2.resize(watermark_image, (roi.shape[1], roi.shape[0]))

# Print the dimensions of the ROI and wat ermark image
print("ROI dimensions:", roi.shape)
print("Watermark image dimensions:", watermark_image_resized.shape)

# Add the watermark to the ROI
result = cv2.addWeighted(roi, 1, watermark_image_resized, 0.3, 0)

# Replace the original ROI with the watermarked ROI
original_image[start_y:start_y + watermark_height, start_x:start_x + watermark_width] = result

# Display the watermarked image
cv2.imshow("Watermarked Image", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
