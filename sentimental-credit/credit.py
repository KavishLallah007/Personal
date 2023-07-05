# TODO

def main():
    # prompt user for input
    while True:
        card_num = int(input("Number: "))
        if card_num > 0:
            break

    if valid(card_num):
        brand(card_num)
    else:
        print("INVALID")


# validity check of length and sum
def valid(card_num):
    if (len(str(card_num)) == 13 or len(str(card_num)) == 15 or len(str(card_num)) == 16) and checksum(card_num):
        return True
    else:
        return False


# perform check sum of card number
def checksum(card_num):
    sum = 0
    for i in range(len(str(card_num))):
        if (i % 2 == 0):
            sum += (card_num % 10)
        # perform sum of digits in the "even" position starting from right
        else:
            digit = 2 * (card_num % 10)
            sum += (digit % 10) + (digit // 10)
        card_num //= 10
    return sum % 10 == 0


def brand(card_num):
    # check for AMEX card starting digit
    if (card_num >= 34e13 and card_num < 35e13) or (card_num >= 37e13 and card_num < 38e13):
        print("AMEX")
    # check for MASTERCARD card starting digit
    elif (card_num >= 51e14) and (card_num < 56e14):
        print("MASTERCARD")
    # check for VISA card starting digit
    elif (card_num >= 4e12 and card_num < 5e12) or (card_num >= 4e15 and card_num < 5e15):
        print("VISA")
    else:
        print("INVALID")


main()
