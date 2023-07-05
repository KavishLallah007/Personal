def main():
    time = input("Enter time: ")

    check_time = convert(time)
    
    if check_time >= 7.0 and check_time <= 8.0:
        print("breakfast time")
    if check_time >= 12.0 and check_time <= 13.0:
        print("lunch time")
    if check_time >= 18.0 and check_time <= 19.0:
        print("dinner time")


def convert(time):
    split_time = time.split(":")

    hour = int(split_time[0])
    minutes = int(split_time[1])/60

    result = hour + minutes
    return float(result)


if __name__ == "__main__":
    main()