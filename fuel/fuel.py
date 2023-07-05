while True:
    try:
        # Ask user for input
        fraction = input("Fraction: ")
        if "/" in fraction:
            value = fraction.split("/")

            output = (int(value[0]) / int(value[1])) * 100

            if int(value[0]) > int(value[1]):
                continue
            elif round(output) <= 1:
                print ("E")
                break
            elif round(output) >= 99:
                print ("F")
                break
            else:
                print (f"{round(output)}%")
                break
    except (ValueError, ZeroDivisionError):
        continue