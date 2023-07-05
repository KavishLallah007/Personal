import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    format =  re.search(r"^(([0-9][0-2]?):?([0-5][0-9])?) ([A-P]M) to (([0-9][0-2]?):?([0-5][0-9])?) ([A-P]M)$", s)
    if format:
        hours = format.groups()
        if int(hours[1]) > 12 or int(hours[5]) > 12:
            raise ValueError
        first_time = convert_format(hours[1], hours[2], hours[3])
        second_time = convert_format(hours[5], hours[6], hours[7])
        return first_time + " to " + second_time
    else:
        raise ValueError

def convert_format(hour, minutes, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minutes == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minutes
    return new_time

...


if __name__ == "__main__":
    main()