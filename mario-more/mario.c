#include <cs50.h>
#include <stdio.h>

//function prototype
void brick(int i);

int main(void)
{
    //variables
    int height;

    //user input
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = 1; i <= height; i++)
    {
        //spaces left of pyramid
        for (int space = 1; space <= (height - i); space++)
        {
            printf(" ");
        }

        //print left half of pyramid
        brick(i);

        //space in between
        printf("  ");

        //print right half of pyramid
        brick(i);

        //shift to next line
        printf("\n");
    }
}

//function to print bricks
void brick(int i)
{
    for (int j = 1; j <= i; j++)
    {
        printf("#");
    }
}