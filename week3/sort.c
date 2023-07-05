#include <cs50.h>
#include <stdio.h>

void bubble_sort(int array[], int size);
void merge_sort(int array[], int size);
void merge_sort_recursion(int array[], int l, int r);
void merge_sorted_array(int array[], int l, int m, int r);
void swap(int num1, int num2);

int main(void)
{
    int data[] = {2, 5, 7, 1, 0, 9, 8, 3, 6, 4};
    int length = (sizeof(data)/sizeof(data[0]));

    //bubble_sort(data, length);
    merge_sort(data, length);

    for (int i = 0; i < length; i++)
    {
        printf("%i", data[i]);
    }
    printf("\n");
}

void merge_sort(int array[], int size)
{
    merge_sort_recursion(array, 0, size - 1);
}

void merge_sort_recursion(int array[], int l, int r)
{
    if (l < r)
    {
        int mid = l + (r - l) / 2;

        merge_sort_recursion(array, l, mid);
        merge_sort_recursion(array, mid +1, r);

        merge_sorted_array(array, l, mid, r);
    }
}

void merge_sorted_array(int array[], int l, int m, int r)
{
    int left_length = m - l + 1;
    int right_length = r - m;

    int temp_left[left_length];
    int temp_right[right_length];

    int i, j ,k;

    for (int a = 0; a < left_length; a++)
    {
        temp_left[a] = array[l + a];
    }

    for (int b = 0; b < right_length; b++)
    {
        temp_right[b] = array[m + 1 + b];
    }

    for (i = 0, j = 0, k = l; k <= r; k++)
    {
        if ((i < left_length) && (j >= right_length || temp_left[i] <= temp_right[j]))
        {
            array[k] = temp_left[i];
            i++;
        }
        else
        {
            array[k] = temp_right[j];
            j++;
        }
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