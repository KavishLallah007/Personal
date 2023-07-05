chk_word = "hello"
greet = input("Greeting: ")
intro = greet.lower().strip()

if intro[0] == "h":
    if chk_word in intro:
        print("$0")
    else:
        print("$20")
else:
    print("$100")