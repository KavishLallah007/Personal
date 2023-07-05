import sys

# Command-line argument check
if len(sys.argv) == 2:
    try:
        py_file = sys.argv[1]
        if ".py" in py_file:
            counter = 0
            comments = 0
            blank = 0
            with open(py_file) as file:
                reader = file.readlines()
                for line in reader:
                    # Checking for and removing comments in code
                    if line.isspace():
                        counter += 0
                    elif line.lstrip().startswith("#"):
                        counter += 0
                    else:
                        counter += 1
                print(counter)
        else:
            print("Not a Python file")
            sys.exit(1)
    except:
        print("File does not exist")
        sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    print("Too few command-line arguments")
    sys.exit(1)

