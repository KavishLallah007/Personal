// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <strings.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = LENGTH * ('z' + 1);
int countWord = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hashNumber = hash(word);

    //create a pointer variable
    node *cursor = table[hashNumber];

    //loop until the end of list
    while (cursor != NULL)
    {
        //check if word are the same
        if (strcasecmp(cursor -> word, word) == 0)
        {
            return true;
        }
        //move pointer to next node
        cursor = cursor -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return (sum % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *DictFile = fopen(dictionary, "r");

    if (DictFile == NULL)
    {
        return false;
    }

    char str[LENGTH + 1];

    while (fscanf(DictFile, "%s", str) != EOF)
    {
        node *temp = malloc(sizeof(node));

        if (temp == NULL)
        {
            return false;
        }

        strcpy(temp -> word, str);
        temp -> next = NULL;

        int hashNum = hash(str);

        if (table[hashNum] == NULL)
        {
            table[hashNum] = temp;
        }
        else
        {
            temp -> next = table[hashNum];
            table[hashNum] = temp;
        }
        countWord++;
    }
    fclose(DictFile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return countWord;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *head = table[i];
        node *cursor = head;
        node *temp = head;

        while (cursor != NULL)
        {
            cursor = cursor -> next;
            free(temp);
            temp = cursor;
        }
    }
    return true;
}
