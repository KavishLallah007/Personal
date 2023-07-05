# Initialize variable and constant
vowels = ["A", "E", "I", "O", "U"]
output_txt = ""

input_txt = input("Input: ")

for letter in input_txt:
    if letter.upper() in vowels:
        output_txt += ""
    else:
        output_txt += letter
print(output_txt)