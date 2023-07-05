#include <stdio.h>

int main(void)
{
    /*
    //1st example
    int n = 50;
    int *p = &n;
    printf("%i\n", *p);
    */

    /*
    //2nd example pointers in string data type
    char *s = "HI!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    */

    //3rd example pointer arithmetics
    char *s = "HI!";
    printf("%s\n", s);
    printf("%s\n", s + 1);
    printf("%s\n", s + 2);
}