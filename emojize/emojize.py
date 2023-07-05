import emoji

# Ask user for input
alias = input("Emoji: ")

emojized = emoji.emojize(alias)

print(f"Emojized: {emojized}")