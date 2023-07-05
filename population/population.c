#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start;
    int end;
    int year = 0;
    int death;
    int birth;
    // TODO: Prompt for start size
    do
    {
        start = get_int("What is the starting population size? ");
    }
    while (start < 9);

    // TODO: Prompt for end size
    do
    {
        end = get_int("What is the ending population size? ");
    }
    while (end < start);

    // TODO: Calculate number of years until we reach threshold
    if (start == end)
    {
        printf("Years: %i\n", year);
    }
    else
    {
        do
        {
            death = start / 4;
            birth = start / 3;

            start = start + birth - death;
            year++;
        }
        while (start < end);

        // TODO: Print number of years
        printf("Years: %i\n", year);
    }
}
