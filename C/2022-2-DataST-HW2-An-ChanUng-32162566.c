/* An-ChanUng 32162566
*/
#include <stdio.h>

typedef struct result_type {
    unsigned int student_number;
    char name[30];
    int grading[4];
}result_type;

void insert_student(result_type* std_array, int num)
{
   

    scanf("%d %s %d %d %d %d", &std_array[num].student_number, std_array[num].name,
        &std_array[num].grading[0], &std_array[num].grading[1], &std_array[num].grading[2], &std_array[num].grading[3]);
    
}

void print_students(result_type* std_array)
{
    int i;
    for (i = 0; i < 4; i++)
    {
        int sum = std_array[i].grading[0] + std_array[i].grading[1] + std_array[i].grading[2] + std_array[i].grading[3];
        printf("%d, %s, %d \n", std_array[i].student_number, std_array[i].name, sum);
    }
}

int main(void)
{
    result_type std_array[4];

    int i;
    
    for (i = 0; i < 4; i++)
        insert_student(std_array, i);

    print_students(std_array);

    return 0;
}
