# what are the width and height
# of an image?

from PIL import Image

image = Image.open("code/Image/NTNU_ME.jpg")
width,height = image.size

print(f"{width}*{height} pixels")

# Output:
# 224*225 pixels
