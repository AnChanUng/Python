#include <stdio.h>

int main(void)
{
	int total=0;
	int num=1;
	
	while(num!=0)
	{
		printf("���� �Է�(o to quit) : ");
		scanf("%d", &num);
		total+=num;
	}
	printf("�Էµ� ������ �� ��: %d \n", total);
	return 0;	
} 
