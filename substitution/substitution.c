#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool key_validity(string key);

int main(int argc, string argv[])
{

    string key = argv[1];
    int index, length;

    if (argc == 2 && key_validity(key))
    {
        string plaintext = get_string("plaintext: ");
        length = strlen(plaintext);
        char ciphertext[length + 1];

        for (int i = 0; i < length; i++)
        {
            if (isupper(plaintext[i]))
            {
                index = plaintext[i] - 65;
                ciphertext[i] = key[index];
                if (islower(ciphertext[i]))
                {
                    ciphertext[i] -= 32;
                }
            }
            else if (islower(plaintext[i]))
            {
                index = plaintext[i] - 97;
                ciphertext[i] = key[index];
                if (isupper(ciphertext[i]))
                {
                    ciphertext[i] += 32;
                }
            }
            else
            {
                ciphertext[i] = plaintext[i];
            }
        }
        ciphertext[length] = '\0';
        printf("ciphertext: %s\n", ciphertext);
    }
    else
    {
        return 1;
    }
}

//check key validity
bool key_validity(string key)
{
    int length;

    length = strlen(key);

    if (length != 26)
    {
        printf("Usage: ./substitution key\n");
        return false;
    }
    else
    {
        for (int i = 0; i < length; i++)
        {
            key[i] = toupper(key[i]);
        }

        for (int i = 0; i < length; i++)
        {
            //check for alphabetic characters only
            if (!isalpha(key[i]))
            {
                printf("Key must only contain alphabetic characters.\n");
                return false;
            }
            //check for duplicate characters
            for (int j = i + 1; j < length; j++)
            {
                if (key[i] == key[j])
                {
                    printf("Key must not contain duplicates.\n");
                    return false;
                }
            }
        }
        return true;
    }
}