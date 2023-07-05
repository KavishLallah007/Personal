# Initialize values
price = 50
paid = 0
due = 0
owed = 0

while paid < price:
    coin = int(input("Insert coin: "))

    if coin in [25, 10, 5]:
        paid += coin
        if paid < price:
            due = price - paid
            print(f"Amount Due: {due}")
        else:
            owed = paid - price
            print(f"Change Owed: {owed}")
    else:
        print("Amount Due: 50")