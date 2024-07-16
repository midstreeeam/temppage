from PIL import Image

# List of image file paths
image_paths = [
    "img/maibi-01.png",
    "img/maibi-02.png",
    "img/maibi-03.png",
    "img/maibi-04.png",
    "img/maibi-05.png",
    "img/maibi-06.png",
    "img/maibi-07.png",
    "img/maibi-08.png",
    "img/maibi-09.png",
    "img/maibi-10.png",
    "img/maibi-11.png",
    "img/maibi-12.png",
    "img/maibi-13.png",
    "img/maibi-14.png",
    "img/maibi-15.png",
]

# Open images and store them in a list
images = [Image.open(path) for path in image_paths]

# Calculate the total height and max width for the final image
total_height = sum(img.height for img in images)
max_width = max(img.width for img in images)

# Create a new blank image with the calculated dimensions
combined_image = Image.new('RGB', (max_width, total_height))

# Paste each image into the combined image
current_y = 0
for img in images:
    combined_image.paste(img, (0, current_y))
    current_y += img.height

# Save the combined image
output_path = "combined_image.png"
combined_image.save(output_path)

print(f"Combined image saved as {output_path}")
