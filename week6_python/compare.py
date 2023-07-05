from cs50 import get_int

def main():
    string_compare()

def string_compare():
    s = input("s: ")
    t = input("t: ")
    if s == t:
        print("Same")
    else:
        print("Different")




def int_compare():
    x = get_int("x: ")
    y = get_int("y: ")

    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")


main()