def main():
    height = get_height()
    vertical(height)
    horizontal(height)
    alt_horizontal(height)
    block(height)


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")

def vertical(n):
    # display vertically, default \n in print
    print("Vertical for loop")
    for i in range(n):
        print("#")

def horizontal(n):
    # display horizontally, override end of line
    print("Horizontal for loop")
    for i in range(n):
        print("?", end = "")
    print()

def alt_horizontal(n):
    # display horizontally, alternative
    print("Horizontal alternative print("'"?"'" * n)")
    print("?" * n)

def block(n):
    # display block, override end of line
    print("block")
    for i in range(n):
        for j in range(n):
            print("#", end = "")
        print()

main()