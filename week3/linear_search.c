#include <cs50.h>
#include <stdio.h>

bool linear_search(int num, int array[], int size);

int main(void)
{
    int number = get_int("Number: ");
    int data[] = {1, 5, 10, 20, 50, 100, 500};
    int length = (sizeof(data)/sizeof(data[0]));


    if(linear_search(number, data, length))
    {
        printf("number found!\n");
    }
    else
    {
        printf("number not found!\n");
    }


}

bool linear_search(int num, int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        if (num == array[i])
        {
            return true;
        }
    }
    return false;
}