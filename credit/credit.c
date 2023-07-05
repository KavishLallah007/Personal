#include <cs50.h>
#include <stdio.h>

//functions prototypes
int card_length(long card_num);
bool valid(long card_num);
bool checksum(long card_num);
void brand(long card_num);

int main(void)
{
    //Variables
    long card_num;

    //prompt user for input
    do
    {
        card_num = get_long("Number: ");
    }
    while (card_num < 0);

    //output
    if (valid(card_num))
    {
        brand(card_num);
    }
    else
    {
        printf("INVALID\n");
    }

}

// validity check of length and sum
bool valid(long card_num)
{
    if ((card_length(card_num) == 13 || card_length(card_num) == 15 || card_length(card_num) == 16) && checksum(card_num))
    {
        return true;
    }
    else
    {
        return false;
    }
}

//return card number length
int card_length(long card_num)
{
    int length = 0;
    while (card_num != 0)
    {
        card_num /= 10;
        length++;
    }
    return length;
}

//perform check sum of card number
bool checksum(long card_num)
{
    int sum = 0;
    int i = 0;
    while (card_num != 0)
    {
        if (i % 2 == 0)
        {
            sum += (card_num % 10);
        }
        //perform sum of digits in the "even" position starting from right
        else
        {
            int digit = 2 * (card_num % 10);
            sum += (digit % 10) + (digit / 10);
        }
        card_num = card_num / 10;
        i++;
    }
    return sum % 10 == 0;
}

//print the brand of card
void brand(long card_num)
{
    //check for AMEX card starting digit
    if ((card_num >= 34e13 && card_num < 35e13) || (card_num >= 37e13 && card_num < 38e13))
    {
        printf("AMEX\n");
    }
    //check for MASTERCARD card starting digit
    else if ((card_num >= 51e14) && (card_num < 56e14))
    {
        printf("MASTERCARD\n");
    }
    //check for VISA card starting digit
    else if (((card_num >= 4e12) && (card_num < 5e12)) || ((card_num >= 4e15) && (card_num < 5e15)))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}