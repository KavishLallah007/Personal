def main():
    # Ask user for input
    text = input("Enter emoticon: ")

    emoji = convert(text)

    print(emoji)

# Function to convert emoticon ti emoji
def convert (emoticon):

    if ":)" in emoticon:
        emoticon = emoticon.replace(":)", "🙂")

    if ":(" in emoticon :
        emoticon = emoticon.replace(":(","🙁")
    return emoticon

main()