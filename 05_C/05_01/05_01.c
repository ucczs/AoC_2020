#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TEST_RUN 0

#if( TEST_RUN == 1 )
    #define LINE_LENGTH 14
    #define NUMBER_BOARDING_PASSES 4
#else
    #define LINE_LENGTH 14
    #define NUMBER_BOARDING_PASSES 782
#endif

#define NUMBER_ROW_DIVIDER 7
#define NUMBER_SEAT_DIVIDER 3

typedef struct{
    char row_div[NUMBER_ROW_DIVIDER];
    char seat_div[NUMBER_SEAT_DIVIDER];
    int row;
    int column;
    int seatID;
}boarding_pass_type;

#define max(a,b) (((a) > (b)) ? (a) : (b))


int getNumber(int lowerStart, int upperStart, int iterations, char* divider_char, char lower_char)
{
    int row_min = lowerStart;
    int row_max = upperStart;
    int diff = upperStart - lowerStart;

    for (int i = 0; i < iterations; i++)
    {
        if (divider_char[i] == lower_char)
        {
            row_min = row_min;
            row_max = row_max - (int)(diff/2.0 + 0.5);
        }
        else
        {
            row_min = row_max - (int)(diff/2.0 - 0.5);
            row_max = row_max;
        }

        diff = row_max - row_min;
    }

    return(row_max);
}

void evaluateBoardingPass(boarding_pass_type* boardingPass)
{
    boardingPass->row = getNumber(0, 127, NUMBER_ROW_DIVIDER, &boardingPass->row_div, 'F');
    boardingPass->column = getNumber(0, 7, NUMBER_SEAT_DIVIDER, &boardingPass->seat_div, 'L');
    
    boardingPass->seatID = boardingPass->row * 8 + boardingPass->column;

}

int getHighestID(boarding_pass_type* boardingPass)
{
    int highestID = 0;

    for (int i = 0; i < NUMBER_BOARDING_PASSES; i++)
    {
        highestID = max(highestID, boardingPass[i].seatID);
    }
    return(highestID);
}


int main(int argc, char *argv[]) {
    FILE* fp;
    char line[LINE_LENGTH];

#if( TEST_RUN == 1 )
    fp = fopen("test.txt", "r");
#else
    fp = fopen("input.txt", "r");
#endif

    if(fp == NULL)
    {
        printf("File could not be opened!");
        exit(1);
    }

    boarding_pass_type boardingPassCollection[NUMBER_BOARDING_PASSES];
    int boardingPassCount = 0;
    
    while(fgets(line, sizeof(line), fp) != NULL)
    {
        //printf("%s", line);

        sscanf(line, "%c%c%c%c%c%c%c%c%c%c", 
            &boardingPassCollection[boardingPassCount].row_div[0],
            &boardingPassCollection[boardingPassCount].row_div[1],
            &boardingPassCollection[boardingPassCount].row_div[2],
            &boardingPassCollection[boardingPassCount].row_div[3],
            &boardingPassCollection[boardingPassCount].row_div[4],
            &boardingPassCollection[boardingPassCount].row_div[5],
            &boardingPassCollection[boardingPassCount].row_div[6],
            &boardingPassCollection[boardingPassCount].seat_div[0],
            &boardingPassCollection[boardingPassCount].seat_div[1],
            &boardingPassCollection[boardingPassCount].seat_div[2]);

        evaluateBoardingPass(&boardingPassCollection[boardingPassCount]);

        boardingPassCount++;
    }

    int result = getHighestID(&boardingPassCollection);
    printf("\nResult 05_01: %d\n", result);

    fclose(fp);
    return(0);
}
