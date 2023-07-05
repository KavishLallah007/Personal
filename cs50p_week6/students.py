import csv

def main():
    write_to_csv()


# Read csv file
def read_csv():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house}")


# Read csv file and sort content
def read_csv_sorted():
    students = []

    with open("students1.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Option 1
            students.append({"name": row["name"], "home": row["home"]})
            # Option 2: students.append(row)


    # lambda functions has no name
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")


# Write to csv file
def write_to_csv():
    name = input("What's your name? ")
    home = input("Where's your home? ")
    with open("students2.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})

if __name__ == "__main__":
    main()