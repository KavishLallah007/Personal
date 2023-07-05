#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{

    typedef uint8_t BYTE;
    BYTE buffer[512];
    int byte_read, counter = 0;
    char filename[8];

    //open memory card
    FILE *f = fopen(argv[1], "r");
    FILE *img = NULL;

    //check for command line arguments
    if (argc != 2)
    {
        printf("USAGE: ./recover IMAGE\n");
        return 1;
    }

    if (f == NULL)
    {
        printf("./recover card.raw");
        return 1;
    }

    //repeat until end of card
    while (1)
    {
        byte_read = fread(buffer, sizeof(BYTE), 512, f);
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {
            //if first JPEG
            if (counter == 0)
            {
                //create file and write
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), byte_read, img);
                counter++;
            }
            //else close file and open a new file to write
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), byte_read, img);
                counter++;
            }
        }
        //if already found jpeg, keep writing to it
        else if (counter != 0)
        {
            fwrite(buffer, sizeof(BYTE), byte_read, img);
            //if reach end of file, close file
            if (byte_read == 0)
            {
                fclose(img);
                fclose(f);
                return 0;
            }
        }
    }
    //close all remaining files
    fclose(img);
    fclose(f);

}