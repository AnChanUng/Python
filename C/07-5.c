#include <stdio.h>

int main(void)
{
	int total=0, i=0;
	int num, input;
	
	printf("�Է��� ������ ����? ");
	scanf("%d", &num);
	
	while(i++<num)
	{
		printf("���� �Է� : ");
		scanf("%d", &input);
		total+=input;	
	} 
	printf("�Է��� ���: %f \n", (double)total/num);
	return 0;
}
