#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

//function prototypes
int count_letters(string word);
int count_words(string text);
int count_sentences(string text);
void grade(float letters, float words, float sentences);

int main(void)
{
    string text;
    int letters, words, sentences;

    //prompt user for input
    do
    {
        text = get_string("Text: ");
    }
    while (strlen(text) == 0);

    //assign values to variables
    letters = count_letters(text);
    words = count_words(text);
    sentences = count_sentences(text);

    //print grade of text
    grade((float)letters, (float)words, (float)sentences);

}

//counting number of letters
int count_letters(string word)
{
    int letters = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        if (isalpha(word[i]))
        {
            letters += 1;
        }
    }
    return letters;
}

//counting number of words
int count_words(string text)
{
    int words = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            words ++;
        }
    }
    words++;
    return words;
}

//counting number of sentences
int count_sentences(string text)
{
    int sentence = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentence++;
        }
    }
    return sentence;
}

//calculating grade of Text
void grade(float letters, float words, float sentences)
{
    double L, S;

    L = letters / words * 100;
    S = sentences / words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}