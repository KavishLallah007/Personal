#include <cs50.h>
#include <stdio.h>

bool binary_search(int num, int array[], int left, int size);
void bubble_sort(int array[], int size);
void swap(int num1, int num2);

int main(void)
{
    int number = get_int("Number: ");
    int data[] = {1, 5, 10, 20, 50, 100, 500};
    int length = (sizeof(data)/sizeof(data[0]));

    bubble_sort(data, length);

    if(binary_search(number, data, 0, length))
    {
        printf("number found!\n");
    }
    else
    {
        printf("number not found!\n");
    }


}

bool binary_search(int num, int array[], int left, int size)
{
    int index =  left + (size - left) / 2;

    if (left > size)
    {
        return false;
    }

    if (array[index] == num)
    {
        return true;
    }
    else if (array[index] > num)
    {
        return binary_search(num, array, left, (index - 1));
    }
    else if (array[index] < num)
    {
        return binary_search(num, array, (index + 1), size);
    }
    else
    {
        return false;
    }
}

void bubble_sort(int array[], int size)
{
    int temp, i = 0;
    bool swapped = false;

    do
    {
        swapped = false;
        for (int j = 0; j < (size - 1 - i); j++)
        {
            if (array[j] > array[j + 1])
            {
                swap(array[j], array[j + 1]);
                swapped = true;
            }
        }
        i++;
    }
    while (swapped);
}

void swap(int num1, int num2)
{
    int temp;
    temp = num1;
    num1 = num2;
    num2 = temp;
}