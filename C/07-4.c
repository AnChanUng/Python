#include <stdio.h>

int main(void)
{
	int num;
	int i=9;
	
	printf("�������� ����� �� �Է�: ");
	scanf("%d", &num);
	
	while(i>0)
	{
		printf("%dx%d=%d \n", num, i, num*i);
		i--;
	}
	return 0;
}
