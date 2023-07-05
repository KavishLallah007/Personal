#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0, swap = width - 1; j < width; j++)
        {
            image[i][j] = temp[i][swap];
            swap--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    float total_Red, total_Green, total_Blue;
    int count =  0;
    total_Red = total_Green = total_Blue = 0;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            for (int arr_row = i - 1; arr_row <= i + 1; arr_row++)
            {
                for (int arr_col = j - 1; arr_col <= j + 1; arr_col++)
                {
                    if (arr_col < width && arr_row < height && arr_col >= 0 && arr_row >= 0)
                    {
                        total_Red += temp[arr_row][arr_col].rgbtRed;
                        total_Green += temp[arr_row][arr_col].rgbtGreen;
                        total_Blue += temp[arr_row][arr_col].rgbtBlue;
                        count++;
                    }
                }
            }
            image[i][j].rgbtRed = round(total_Red / count);
            image[i][j].rgbtGreen = round(total_Green / count);
            image[i][j].rgbtBlue = round(total_Blue / count);
            count = 0;
            total_Red = total_Green = total_Blue = 0;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp_img[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp_img[i][j] = image[i][j];
        }
    }

    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int row[3] = {i - 1, i, i + 1};
            int col[3] = {j - 1, j, j + 1};
            int gxRed, gxGreen, gxBlue;
            int gyRed, gyGreen, gyBlue;
            gxRed = gxGreen = gxBlue = 0;
            gyRed = gyGreen = gyBlue = 0;

            for (int row_count = 0; row_count < 3; row_count++)
            {
                for (int col_count = 0; col_count < 3; col_count++)
                {
                    int nrow = row[row_count];
                    int ncol = col[col_count];

                    RGBTRIPLE pixel = temp_img[nrow][ncol];

                    if (nrow < height && nrow >= 0 && ncol < width && ncol >= 0)
                    {
                        gxRed += pixel.rgbtRed * gx[row_count][col_count];
                        gxGreen += pixel.rgbtGreen * gx[row_count][col_count];
                        gxBlue += pixel.rgbtBlue * gx[row_count][col_count];

                        gyRed += pixel.rgbtRed * gy[row_count][col_count];
                        gyGreen += pixel.rgbtGreen * gy[row_count][col_count];
                        gyBlue += pixel.rgbtBlue * gy[row_count][col_count];
                    }
                }
            }
            int new_Red = round(sqrt(gxRed * gxRed + gyRed * gyRed));
            int new_Green = round(sqrt(gxGreen * gxGreen + gyGreen * gyGreen));
            int new_Blue = round(sqrt(gxBlue * gxBlue + gyBlue * gyBlue));

            image[i][j].rgbtRed = new_Red > 255 ? 255 : new_Red;
            image[i][j].rgbtGreen = new_Green > 255 ? 255 : new_Green;
            image[i][j].rgbtBlue = new_Blue > 255 ? 255 : new_Blue;
        }
    }
    return;
}
