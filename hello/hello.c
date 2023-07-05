#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //taking a string as user input
    string name = get_string("What is your name? ");

    //Output
    printf("hello, %s\n", name);
}