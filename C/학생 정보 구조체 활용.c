#include <stdio.h>
#include <stdlib.h>

struct stduent {
	int number;
	char name[10];
	double grade;	
};

int main(void)
{
	struct stduent s;
	
	printf("�й��� �Է��ϼ��� : ");
	scanf("%d", &s.number);
	printf("�̸��� �Է��ϼ��� :");
	scanf("%s", s.name);
	printf("������ �Է��ϼ��� : ");
	scanf("%1f", &s.grade);
	
	printf("�й� : %d\n", s.number);
	printf("�̸� : %s\n", s.name);
	printf("���� : %.1f\n", s.grade);
	return 0; 
}
