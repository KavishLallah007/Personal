import sys
import os
from PIL import Image, ImageOps

def main():
    check_argv()

    # Check if image opens
    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open shirt.png and resize muppet to fit image
    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(image_file, size)
    muppet.paste(shirt, shirt)

    # Create after.jpg
    muppet.save(sys.argv[2])


# Command-line argument check
def check_argv():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    img1 = os.path.splitext(sys.argv[1])
    img2 = os.path.splitext(sys.argv[2])

    if img1[1] not in [".jpg", ".jpeg", ".png"] or img2[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    if img1[1].lower() != img2[1].lower():
        sys.exit("Input and output have different extensions")




if __name__ == "__main__":
    main()