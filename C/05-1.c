#include <stdio.h>

int main(void)
{
	int x1, y1;
	int x2, y2;
	int area;

	printf("�� ����� x, y ��ǥ: ");
	scanf("%d %d", &x1, &y1);
	printf("�� �ϴ��� x, y ��ǥ: ");
	scanf("%d %d", &x2, &y2);
	area = (x2 - x1) * (y2 - y1);
	printf("�� ���� �̷�� ���簢���� ���̴� %d�Դϴ�. \n", area);
	return 0;
}
