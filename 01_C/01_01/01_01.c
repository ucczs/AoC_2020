#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TEST_RUN 0

#if( TEST_RUN == 1 )
    #define LINE_LENGTH 6
    #define NUMBER_TOTAL 6
#else
    #define LINE_LENGTH 6
    #define NUMBER_TOTAL 200
#endif


int main(int argc, char *argv[]) {
    FILE* fp;
    char line[LINE_LENGTH];
    int numbers[NUMBER_TOTAL];
    int idx = 0;

#if( TEST_RUN == 1 )
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\01_C\\01_01\\test.txt", "r");
#else
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\01_C\\01_01\\input.txt", "r");
#endif

    if(fp == NULL)
    {
        printf("File could not be opened!");
        exit(1);
    }

    while(fgets(line, sizeof(line), fp) != NULL)
    {
        numbers[idx] = atoi(line);

        idx++;
    }

    for (int firstNo = 0; firstNo < NUMBER_TOTAL; firstNo++)
    {
        for (int secondNo = firstNo+1; secondNo < NUMBER_TOTAL; secondNo++)
        {
            if (numbers[firstNo] + numbers[secondNo] == 2020)
                {
                    int result = numbers[firstNo] * numbers[secondNo];
                    printf("Result: %d\n",result);
                }
        }
    }

    return(0);
}