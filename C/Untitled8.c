#include <stdio.h>

int main(void)
{
	int num;
	prinf("���� �Է�: ");
	scanf("%d", &num);
	num = ~num;
	num = num + 1;
	printf("��ȣ�� �ٲ� ��� : %d \n", num);
	return 0;	
} 
