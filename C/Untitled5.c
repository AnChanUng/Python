#include<stdio.h>

int main(void)
{
	int num1, num2;
	printf("두 정수를 입력하세요. :");
	scanf("%d, %d", &num1, &num2);
	printf("몫 : %d \n", num1 / num2);
	printf("나머지 : %d", num1 % num2); 
	return 0;
}
