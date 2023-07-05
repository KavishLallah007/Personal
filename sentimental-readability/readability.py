# TODO

def main():
    text = ""

    # prompt user for input
    while (len(text) == 0):
        text = input("Text: ")

    # assign values to variables
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # print grade of text
    grade(letters, words, sentences)


# counting number of letters
def count_letters(word):
    letters = 0
    for i in range(len(word)):
        if (word[i] >= "a" and word[i] <= "z") or (word[i] >= "A" and word[i] <= "Z"):
            letters += 1
    return letters


# counting number of words
def count_words(text):
    words = 0
    for i in range(len(text)):
        if (text[i] == " "):
            words += 1
    words += 1
    return words


# counting number of sentences
def count_sentences(text):
    sentence = 0
    for i in range(len(text)):
        if (text[i] == '.' or text[i] == '!' or text[i] == '?'):
            sentence += 1
    return sentence


# calculating grade of Text
def grade(letters, words, sentences):
    L = letters / words * 100
    S = sentences / words * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if (index > 16):
        print("Grade 16+")
    elif (index < 1):
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


main()

