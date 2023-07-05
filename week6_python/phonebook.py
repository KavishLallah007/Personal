import csv


def main():
    csv_file()



def csv_file():
    with open("phonebook.csv", "a") as file:

        name = input("Name: ")
        number = input("Number: ")

        writer = csv.DictWriter(file, fieldnames = ["name", "number"])
        writer.writerow({"name": name, "number": number})


def dict_search():
    #dictionary either use people = dict() or people = {}
    people = {
        "Carter": "+1-617-495-1000",
        "David": "+1-949-468-2750"
    }

    name = input("Name: ")
    if name in people:
        number = people[name]
        print(f"Number: {number}")


main()