#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TEST_RUN 0

#if (TEST_RUN == 1)
#define LINE_LENGTH 18
#define RULES_COUNT 3
#else
#define LINE_LENGTH 40
#define RULES_COUNT 1000
#endif

#define PASSWORD_LENGTH 25

typedef struct
{
    char letterRule[1];
    int minimum_occurance;
    int maximum_occurance;
    char password[PASSWORD_LENGTH];
} passwordRule_type;

bool checkRule(char *line)
{
    int letter_count = 0;
    bool ret_val = true;

    passwordRule_type *newRule = (passwordRule_type *)calloc(1, sizeof(passwordRule_type));

    sscanf(line, "%d-%d %c: %s", &newRule->minimum_occurance, &newRule->maximum_occurance, &newRule->letterRule[0],
           &newRule->password[0]);

    for (int i = 0; i < PASSWORD_LENGTH; i++)
    {
        if (newRule->password[i] == newRule->letterRule[0])
        {
            letter_count++;
        }
    }

    if (letter_count < newRule->minimum_occurance || letter_count > newRule->maximum_occurance)
    {
        ret_val = false;
    }

    free(newRule);

    return (ret_val);
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char line[LINE_LENGTH];

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

    int rule_true_count = 0;

    while (fgets(line, sizeof(line), fp) != NULL)
    {
        bool rule_correct;
        rule_correct = checkRule(&line[0]);

        if (rule_correct == true)
        {
            rule_true_count++;
        }
    }

    printf("\nResult 02_01: %d\n", rule_true_count);

    return (0);
}
