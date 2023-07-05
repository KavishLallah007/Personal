import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Checks if start with 2 letters and length between 1 and 6
    if s[0:2].isalpha() and len(s) > 1 and len(s) < 7:
        for char in range(len(s)):

            # Check for numeric value in middle
            if char < len(s) - 1:
                if s[char].isnumeric() and s[char + 1].isalpha():
                    return False
            else:
                if s[char].isnumeric() and s[len(s)-1].isalpha():
                    return False

            # Check if first number is zero
            if s[char].isnumeric() and s[char - 1].isalpha() and s[char] == '0':
                return False

            # Check for punctuations and spaces
            if s[char] == " " or s[char] in string.punctuation:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()