# Ask user for input
text = input("Enter text: ")
length= len(text)

# Initialize output variable
temp = ""

# Loop on all characters in input
for letter in range(length):
    # Check character uppercase
    if text[letter].isupper():
        temp = temp + "_"
        print(text[letter])
    temp = temp + text[letter].lower()
print(temp)