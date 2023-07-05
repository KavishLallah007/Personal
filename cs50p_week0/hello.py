def main():
    # Ask user for input
    name = input("What's your name? ")

    # Split user's name into first name and last name
    first, last = name.split(" ")

    print(f"hello, {first}")
    
    # Function call
    hello(name)
    hello()

# creating functions and set default values in case no input provided
def hello(to="world"):



    # Remove whitespace from str and capitalize user's name
    to = to.strip().title()

    # Output
    print(f"hello, {to}")

    # Replace the seperator in print()
    print("hello,", to, sep="?" )


main()