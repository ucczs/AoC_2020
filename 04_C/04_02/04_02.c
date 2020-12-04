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

#define LENGTH_FILED_NAMES 3
#define LENGTH_HAIR_COLOR 3

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


bool checkForNumberRange(int lower_border, int upper_border, char* charInput)
{
    long number = strtol(charInput, NULL, 10);
    bool ret_val;

    if( number >= lower_border && number <= upper_border)
    {
        ret_val = true;
    }
    else
    {
        ret_val = false;
    }

    return(ret_val);
}


void extractFieldsFromLine(char line[LINE_LENGTH], passport_type* current_passport)
{
    char* line_pos = line;

    while (line_pos != NULL)
    {
        // byr_b
        if(strncmp(line_pos, "byr", LENGTH_FILED_NAMES) == 0)
        {
            current_passport->byr_b = checkForNumberRange(1920, 2002, &line_pos[4]);
        }
        // iyr_b
        else if (strncmp(line_pos, "iyr", LENGTH_FILED_NAMES) == 0)
        {
            current_passport->iyr_b = checkForNumberRange(2010, 2020, &line_pos[4]);
        }
        // eyr_b
        else if (strncmp(line_pos, "eyr", LENGTH_FILED_NAMES) == 0)
        {
            current_passport->eyr_b = checkForNumberRange(2020, 2030, &line_pos[4]);
        }
        // hgt_b
        else if (strncmp(line_pos, "hgt", LENGTH_FILED_NAMES) == 0)
        {
            // inche
            if (line_pos[6] == 'i')
            {
                current_passport->hgt_b = checkForNumberRange(59, 76, &line_pos[4]);
            }
            // cm
            else if (line_pos[7] == 'c')
            {
                current_passport->hgt_b = checkForNumberRange(150, 193, &line_pos[4]);
            }
            else
            {
                current_passport->hgt_b = false;
            }
        }
        // hcl_b
        else if (strncmp(line_pos, "hcl", LENGTH_FILED_NAMES) == 0)
        {
            int hairColorLength = 6;

            if (line_pos[4] == '#')
            {
                current_passport->hcl_b = true;

                for (int i = 0; i < hairColorLength; i++)
                {   
                    int ascii_val = (int)line_pos[5+i];
                    if( ascii_val < (int)'0' ||
                        ascii_val > (int)'9' && ascii_val < (int)'a' ||
                        ascii_val > (int)'f')
                    {
                        current_passport->hcl_b = false;
                    }
                }
            }
            else
            {
                current_passport->hcl_b = false;
            }
        }
        // ecl_b
        else if (strncmp(line_pos, "ecl", LENGTH_FILED_NAMES) == 0)
        {
            if(strncmp(&line_pos[4], "amb", LENGTH_HAIR_COLOR) == 0)
            {
                current_passport->ecl_b = true;
            }
            else if (strncmp(&line_pos[4], "blu", LENGTH_HAIR_COLOR) == 0)
            {
                current_passport->ecl_b = true;
            }
            else if (strncmp(&line_pos[4], "brn", LENGTH_HAIR_COLOR) == 0)
            {
                current_passport->ecl_b = true;
            }
            else if (strncmp(&line_pos[4], "gry", LENGTH_HAIR_COLOR) == 0)
            {
                current_passport->ecl_b = true;
            }
            else if (strncmp(&line_pos[4], "grn", LENGTH_HAIR_COLOR) == 0)
            {
                current_passport->ecl_b = true;
            }
            else if (strncmp(&line_pos[4], "hzl", LENGTH_HAIR_COLOR) == 0)
            {
                current_passport->ecl_b = true;
            }
            else if (strncmp(&line_pos[4], "oth", LENGTH_HAIR_COLOR) == 0)
            {
                current_passport->ecl_b = true;
            }
            else
            {
                current_passport->ecl_b = false;
            }
        }
        // pid_b
        else if (strncmp(line_pos, "pid", LENGTH_FILED_NAMES) == 0)
        {
            current_passport->pid_b = true;
            int lengthPassportID = 9;

            for (int i = 0; i < lengthPassportID; i++)
            {   
                int ascii = (int)line_pos[4+i];
                if( ascii < (int)'0' ||
                    ascii > (int)'9')
                {
                    current_passport->pid_b = false;
                }
            }

            // check if ID is longer than 9 characters
            if(line_pos[LENGTH_FILED_NAMES+1+lengthPassportID] != ' ' && line_pos[LENGTH_FILED_NAMES+1+lengthPassportID] != '\n')
            {
                current_passport->pid_b = false;
            }
        }
        // cid_b
        else if (strncmp(line_pos, "cid", LENGTH_FILED_NAMES) == 0)
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
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\04_C\\04_02\\test.txt", "r");
#else
    fp = fopen("D:\\Creativity\\Advent_of_Code\\AoC_2020\\04_C\\04_02\\input.txt", "r");
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

        if (line[0] == '\n')
        {
            passport_idx++;
        }
        else
        {
            extractFieldsFromLine(&line[0], &passportCollection[passport_idx]);
        }
    }

    checkValidStatusOfPassports(&passportCollection[0]);
    int results = getValidPassportsCount(&passportCollection[0]);

    printf("\nValid Passports: %d", results);

    fclose(fp);
    return(0);
}
