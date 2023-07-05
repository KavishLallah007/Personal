def main():
    # Asking for user input
    greet = input("Greeting: ")
    print(f"${value(greet)}")


def value(greeting):
    chk_word = "hello"
    # Cast to lowercase and remoting any spaces to left and right
    intro = greeting.lower().strip()

    # Check if start with "h"
    if intro[0] == "h":
        # Check if word is "hello"
        if chk_word in intro:
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()