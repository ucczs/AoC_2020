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
#define NUMBER_SEATS_PER_ROW 8

typedef struct{
    char row_div[NUMBER_ROW_DIVIDER];
    char seat_div[NUMBER_SEAT_DIVIDER];
    int row;
    int column;
    int seatID;
}boarding_pass_type;


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
    
    boardingPass->seatID = boardingPass->row * NUMBER_SEATS_PER_ROW + boardingPass->column;

}

int getHighestRow(boarding_pass_type* boardingPass)
{
    int highestRow = 0;

    for (int i = 0; i < NUMBER_BOARDING_PASSES; i++)
    {
        if( boardingPass[i].row > highestRow)
        {
            highestRow = boardingPass[i].row;
        }
    }
    return(highestRow);
}

int findRowWithMissingSeat(boarding_pass_type* boardingPassCollection)
{
    int highestRow = getHighestRow(&boardingPassCollection);
    int rowWithMissingSeat;

    for (int row_cnt = 0; row_cnt < highestRow; row_cnt++)
    {
        int foundSeatsInRow = 0;
        for (int i = 0; i < NUMBER_BOARDING_PASSES; i++)
        {
            if (boardingPassCollection[i].row == row_cnt)
            {
                foundSeatsInRow++;
            }
        }
        if (foundSeatsInRow < NUMBER_SEATS_PER_ROW && foundSeatsInRow > 0)
        {
            rowWithMissingSeat = row_cnt;
        }
    }

    return(rowWithMissingSeat);
}

int findMissingSeatInRow(boarding_pass_type* boardingPassCollection, int row)
{
    bool seats_found[NUMBER_SEATS_PER_ROW] = {false};
    int missing_seat;

    for (int i = 0; i < NUMBER_BOARDING_PASSES; i++)
    {
        if (boardingPassCollection[i].row == row)
        {
            seats_found[boardingPassCollection[i].column] = true;
        }
    }

    for (int i = 0; i < NUMBER_SEATS_PER_ROW; i++)
    {
        if (seats_found[i] == false)
        {
            missing_seat = i;
        }
    }
    
    return(missing_seat);
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char line[LINE_LENGTH];

#if( TEST_RUN == 1 )
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\05_C\\05_01\\test.txt", "r");
#else
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\05_C\\05_01\\input.txt", "r");
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
        printf("%s", line);

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


    int myRow = findRowWithMissingSeat(&boardingPassCollection);
    int mySeat = findMissingSeatInRow(&boardingPassCollection, myRow);
    int myID = NUMBER_SEATS_PER_ROW * myRow + mySeat;

    printf("\nMy seat is at row %d, seat number %d, boarding ID %d", myRow, mySeat, myID);

    fclose(fp);
    return(0);
}
