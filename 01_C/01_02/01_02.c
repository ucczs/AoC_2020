#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define TEST_RUN 0

#if (TEST_RUN == 1)
#define LINE_LENGTH 6
#define NUMBER_TOTAL 6
#else
#define LINE_LENGTH 6
#define NUMBER_TOTAL 200
#endif

int main(int argc, char *argv[])
{
    FILE *fp;
    char line[LINE_LENGTH];
    int numbers[NUMBER_TOTAL];
    int idx = 0;

#if (TEST_RUN == 1)
    fp = fopen("test.txt", "r");
#else
    fp = fopen("input.txt", "r");
#endif

    if (fp == NULL)
    {
        printf("File could not be opened!");
        exit(1);
    }

    while (fgets(line, sizeof(line), fp) != NULL)
    {
        numbers[idx] = atoi(line);

        idx++;
    }

    for (int firstNo = 0; firstNo < NUMBER_TOTAL; firstNo++)
    {
        for (int secondNo = firstNo + 1; secondNo < NUMBER_TOTAL; secondNo++)
        {
            for (int thirdNo = secondNo + 1; thirdNo < NUMBER_TOTAL; thirdNo++)
            {
                if (numbers[firstNo] + numbers[secondNo] + numbers[thirdNo] == 2020)
                {
                    int result = numbers[firstNo] * numbers[secondNo] * numbers[thirdNo];
                    printf("Result 01_02: %d\n", result);
                }
            }
        }
    }

    return (0);
}