#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TEST_RUN 1

#if( TEST_RUN == 1 )
    #define LINE_LENGTH 10
#else
    #define LINE_LENGTH 30
#endif


int main(int argc, char *argv[]) {
    FILE* fp;
    char line[LINE_LENGTH];

#if( TEST_RUN == 1 )
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\01_C\\01_02\\test.txt", "r");
#else
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\01_C\\01_02\\input.txt", "r");
#endif

    if(fp == NULL)
    {
        printf("File could not be opened!");
        exit(1);
    }

    while(fgets(line, sizeof(line), fp) != NULL)
    {
        printf("%s", line);
    }



    return(0);
}
