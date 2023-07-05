def main():
    # Ask user for input
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            if "/" in fraction:
                value = fraction.split("/")
                numerator = int(value[0])
                demonimator = int(value[1])
                num_fraction = numerator / demonimator
                if num_fraction <= 1:
                    return num_fraction * 100
                else:
                    fraction = input("Fraction: ")
                    pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if round(percentage) <= 1:
        return "E"
    elif round(percentage) >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()