#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TEST_RUN 0

#if( TEST_RUN == 1 )
    #define LINE_LENGTH 100
    #define PASSPORT_COUNT 4
#else
    #define LINE_LENGTH 100
    #define PASSPORT_COUNT 255
#endif

typedef struct{
    bool byr_b;
    bool iyr_b;
    bool eyr_b;
    bool hgt_b;
    bool hcl_b;
    bool ecl_b;
    bool pid_b;
    bool cid_b;
    bool valid;
}passport_type;


void extractFieldsFromLine(char line[LINE_LENGTH], passport_type* current_passport)
{
    char* line_pos = line;

    while (line_pos != NULL)
    {
        // byr_b
        if(strncmp(line_pos, "byr", 3) == 0)
        {
            current_passport->byr_b = true;
        }
        // iyr_b
        else if (strncmp(line_pos, "iyr", 3) == 0)
        {
            current_passport->iyr_b = true;
        }
        // eyr_b
        else if (strncmp(line_pos, "eyr", 3) == 0)
        {
            current_passport->eyr_b = true;
        }
        // hgt_b
        else if (strncmp(line_pos, "hgt", 3) == 0)
        {
            current_passport->hgt_b = true;
        }
        // hcl_b
        else if (strncmp(line_pos, "hcl", 3) == 0)
        {
            current_passport->hcl_b = true;
        }
        // ecl_b
        else if (strncmp(line_pos, "ecl", 3) == 0)
        {
            current_passport->ecl_b = true;
        }
        // pid_b
        else if (strncmp(line_pos, "pid", 3) == 0)
        {
            current_passport->pid_b = true;
        }
        // cid_b
        else if (strncmp(line_pos, "cid", 3) == 0)
        {
            current_passport->cid_b = true;
        }
        else
        {
            printf("Error in reading in data!\n");
        }

        line_pos = strchr(line_pos, ' ');
        if ( line_pos != NULL)
        {
            line_pos = line_pos + sizeof(char);
        }
    }
}

void checkValidStatusOfPassports(passport_type* passportCollection)
{
    for (int i = 0; i < PASSPORT_COUNT; i++)
    {
        if( passportCollection[i].byr_b == false ||
            passportCollection[i].iyr_b == false ||
            passportCollection[i].eyr_b == false ||
            passportCollection[i].hgt_b == false ||
            passportCollection[i].hcl_b == false ||
            passportCollection[i].ecl_b == false ||
            passportCollection[i].pid_b == false)
        {
            passportCollection[i].valid = false;
        }
        else
        {
            passportCollection[i].valid = true;
        }
    }
}

int getValidPassportsCount(passport_type* passportCollection)
{
    int valid_count = 0;
    for (int i = 0; i < PASSPORT_COUNT; i++)
    {
        if (passportCollection[i].valid == true)
        {
            valid_count++;
        }
    }
    return(valid_count);
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char line[LINE_LENGTH];

#if( TEST_RUN == 1 )
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\04_C\\04_01\\test.txt", "r");
#else
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\04_C\\04_01\\input.txt", "r");
#endif

    if(fp == NULL)
    {
        printf("File could not be opened!");
        exit(1);
    }

    passport_type passportCollection[PASSPORT_COUNT] = {false};
    int passport_idx = 0;

    while(fgets(line, sizeof(line), fp) != NULL)
    {
        printf("%s", line);

        // empty line -> next passport
        if (line[0] == '\n')
        {
            passport_idx++;
        }
        else
        {
            extractFieldsFromLine(&line[0], &passportCollection[passport_idx]);
        }
    }

    checkValidStatusOfPassports(&passportCollection);
    int results = getValidPassportsCount(&passportCollection);

    printf("\nValid Passports: %d", results);

    fclose(fp);
    return(0);
}
