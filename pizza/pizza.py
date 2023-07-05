import sys
import csv
from tabulate import tabulate

def main():
    csv_file = check_argv()
    table = []
    try:
        with open(csv_file) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


# Command-line argument check
def check_argv():
    if len(sys.argv) == 2:
        if ".csv" in sys.argv[1]:
            return sys.argv[1]
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()