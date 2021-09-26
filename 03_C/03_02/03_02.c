#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define TEST_RUN 0

#if (TEST_RUN == 1)
#define LINE_LENGTH 13
#define FOREST_DOWN_SIZE 11
#define FOREST_WIDTH 11
#else
#define LINE_LENGTH 34
#define FOREST_DOWN_SIZE 323
#define FOREST_WIDTH 31
#endif

#define SLOPE_COUNT 5

int slope_right[SLOPE_COUNT];
int slope_down[SLOPE_COUNT];

int defineSlopes()
{
    slope_right[0] = 1;
    slope_down[0] = 1;

    slope_right[1] = 3;
    slope_down[1] = 1;

    slope_right[2] = 5;
    slope_down[2] = 1;

    slope_right[3] = 7;
    slope_down[3] = 1;

    slope_right[4] = 1;
    slope_down[4] = 2;
}

void getCollisionsWithDifferentSlopes(bool map[FOREST_DOWN_SIZE][FOREST_WIDTH], int collision_collection[SLOPE_COUNT])
{
    for (int j = 0; j < SLOPE_COUNT; j++)
    {
        int collision_count = 0;
        int count_right = 0;
        int count_down = 0;

        if (map[count_down][count_right] == true)
        {
            collision_count++;
        }

        for (int i = 0; i < (FOREST_DOWN_SIZE / slope_down[j]) - 1; i++)
        {
            count_down += slope_down[j];
            count_right += slope_right[j];
            count_right = count_right % FOREST_WIDTH;

            if (map[count_down][count_right] == true)
            {
                collision_count++;
            }
        }
        collision_collection[j] = collision_count;
    }
}

long long int getCollisionMultiplikation(int collision_collection[SLOPE_COUNT])
{
    long long int result = collision_collection[0];
    for (int i = 1; i < SLOPE_COUNT; i++)
    {
        result *= collision_collection[i];
    }

    return (result);
}

void readInMap(char *line, bool map[FOREST_DOWN_SIZE][FOREST_WIDTH])
{
    static int depth_count = 0;

    // printf("%s", line);

    for (int i = 0; i < FOREST_WIDTH; i++)
    {
        if (line[i] == '.')
        {
            map[depth_count][i] = false;
        }
        else if (line[i] == '#')
        {
            map[depth_count][i] = true;
        }
    }

    depth_count++;
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char line[LINE_LENGTH];
    bool map[FOREST_DOWN_SIZE][FOREST_WIDTH];

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
        readInMap(&line[0], map);
    }

    defineSlopes();

    int collision_collection[SLOPE_COUNT];
    getCollisionsWithDifferentSlopes(map, collision_collection);

    long long int result = getCollisionMultiplikation(collision_collection);
    printf("Result 03_02: %lld\n", result);

    fclose(fp);
    return (0);
}
