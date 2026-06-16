from PIL import Image

# Open the panoramic town image
img = Image.open("town.jpg")
width, height = img.size

# The town of Gordes is on the left side of the panoramic image.
# We crop a portrait region: from x = 100 to x = 500 (width = 400)
# This gives an aspect ratio of 400:489 (~ 1:1.22), which fits beautifully.
# If we want it even narrower and taller: x = 100 to x = 450 (width = 350)
crop_box = (100, 0, 450, height)
cropped_img = img.crop(crop_box)

# Save the vertical version
cropped_img.save("town_vertical.jpg")
print("Cropped image successfully.")
