# TODO

while True:
    try:
        height = int(input("Height: "))
        if height <= 0 or height > 8:
            print("Invalid input")
        else:
            break
    except ValueError:
        print("invalid input")

for i in range(height):
    print(" " * (height - 1 - i), end="")
    print("#" * (i + 1), end="")
    print(" ", "#" * (i + 1))