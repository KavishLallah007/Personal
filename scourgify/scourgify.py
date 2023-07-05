import sys
import csv

def main():
    check_argv()
    output = []
    try:
        with open(sys.argv[1], "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                last, first = row["name"].split(",")
                output.append({"first": first.lstrip(), "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Write after.csv
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first":row["first"], "last": row["last"], "house": row["house"]})



# Command-line argument check
def check_argv():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()