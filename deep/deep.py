# Ask user for input
text = input("Enter a number: ").lower().strip()

# check if input is 42
if text == "42" or text == "forty-two" or text == "forty two":
    print("Yes")
else:
    print("No")