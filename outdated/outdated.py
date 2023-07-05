months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            if (int(month) >= 1 and int(month) <= 12 ) and (int(day) >= 1 and int(day) <= 31):
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
        elif "," in date and " " in date:
            date = date.replace(",","")
            old_month, day, year = date.split(" ")
            if old_month in months:
                month = months.index(old_month) + 1
            if (month >= 1 and month <= 12 ) and (int(day) >= 1 and int(day) <= 31):
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
    except:
        print()
        pass


