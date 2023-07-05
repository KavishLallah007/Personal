# Ask for user for input
expression = input("Expression: ")

# Assume there is a space in between characters
# Split expression at spaces
components = expression.split(" ")
x = components[0]
y = components[1]
z = components[2]


if y == "+":
    result = float(x) + float(z)

elif y == "-":
    result = float(x) - float(z)

elif y == "*":
    result = float(x) * float(z)

elif y == "/":
    result = float(x) / float(z)

print(f"{result:.1f}")