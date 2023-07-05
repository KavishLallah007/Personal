import sys

from PIL import Image

# code for creating a GIF
images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "Costume.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)