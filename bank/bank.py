# Defining check word
chk_word = "hello"

# Asking for user input
greet = input("Greeting: ")

# Cast to lowercase and remoting any spaces to left and right
intro = greet.lower().strip()

# Check if start with "h"
if intro[0] == "h":
    # Check if word is "hello"
    if chk_word in intro:
        print("$0")
    else:
        print("$20")
else:
    print("$100")