def main():
    read_file()


def write_to_file():
    name = input("What's your name: ")
    # Write to file
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


def read_file():
    names =[]
    # Read from file
    """
    # Can also sort from file directly also
    # For read file no need to add "r" in with open()
    
    with open("names.txt") as file:
        for line in sorted(file):
            print(f"Hello, {name}")

    """
    with open("names.txt", "r") as file:
        for line in file:
            names.append(line.rstrip())

        for name in sorted(names, reverse=True):
            print(f"Hello, {name}")

if __name__ == "__main__":
    main()