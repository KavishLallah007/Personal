def main():
    # Initialize variable and constant
    input_txt = input("Input: ")

    print(shorten(input_txt))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    output_txt = ""
    for letter in word:
        if letter.lower() in vowels:
            output_txt += ""
        else:
            output_txt += letter
    return output_txt


if __name__ == "__main__":
    main()