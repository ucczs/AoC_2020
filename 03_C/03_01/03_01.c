#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TEST_RUN 0

#if( TEST_RUN == 1 )
    #define LINE_LENGTH 13
    #define FOREST_DOWN_SIZE 11
    #define FOREST_WIDTH 11
#else
    #define LINE_LENGTH 34
    #define FOREST_DOWN_SIZE 323
    #define FOREST_WIDTH 31
#endif

#define SLOPE_COUNT 5

#define STEP_SIZE_RIGHT 3
#define STEP_SIZE_DOWN 1


int getCollisions(bool map[FOREST_DOWN_SIZE][FOREST_WIDTH])
{
    int collision_count = 0;
    int count_right = 0;
    int count_down = 0;

    for (int i = 0; i < (FOREST_DOWN_SIZE / STEP_SIZE_DOWN)-1; i++)
    {
        count_down += STEP_SIZE_DOWN;
        count_right += STEP_SIZE_RIGHT;
        count_right = count_right % FOREST_WIDTH;

        if (map[count_down][count_right] == true)
        {
            collision_count++;
        }
    }

    return(collision_count);
}

void readInMap(char* line, bool map[FOREST_DOWN_SIZE][FOREST_WIDTH])
{
    static int depth_count = 0;

    //printf("%s", line);

    for (int i = 0; i < FOREST_WIDTH; i++)
    {
        if( line[i] == '.')
        {
            map[depth_count][i] = false;
        }
        else if( line[i] == '#')
        {
            map[depth_count][i] = true;
        }
    }

    depth_count++;
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char line[LINE_LENGTH];
    bool map[FOREST_DOWN_SIZE][FOREST_WIDTH];

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

    while(fgets(line, sizeof(line), fp) != NULL)
    {
        readInMap(&line[0], map);
    }

    int result = getCollisions(map);

    printf("\nResult 03_01: %d\n", result);

    fclose(fp);
    return(0);
}
