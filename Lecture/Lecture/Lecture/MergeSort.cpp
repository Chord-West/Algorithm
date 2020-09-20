#include <iostream>
#include <vector>

using namespace std;


int number = 8;
vector<int> sorted(8);


void merge(int a[], int m, int middle, int n) {
	int i = m; //2���� ù��°
	int j = middle + 1; // 2���� �ι�°
	int k = m; // ��ģ�迭�� ù��°
	//���� ������� �迭�� ����
	while (i <= middle && j <= n) {
		//�������� k�� �־���
		if (a[i] >= a[j]) {
			sorted[k] = a[i];
			i++;
		}
		else {
			sorted[k] = a[j];
			j++;
		}
		k++;// ���� ���ҿ� ���� ���� �� �ֵ�����
	}
	if (i > middle)  //i �� ���� �迭�� �����������
	{
		for (int t = j; t <= n; t++) {
			sorted[k] = a[t];
			k++;
		}
	}
	else {
		for (int t = i; t <= middle; t++) {
			sorted[k] = a[t];
			k++;
		}
	}
	//���ĵ� �迭�� ����
	for (int t = m; t <= n; t++) {
		a[t] = sorted[t];
	}
}
void mergesort(int a[], int p, int r) {
	if (p < r) {
		int middle = (p + r) / 2;
		mergesort(a, p, middle);
		mergesort(a, middle + 1, r);
		merge(a, p, middle, r);
	}
}

int main() {
	int array[8] = { 7,6,5,8,3,5,9,1 };
	mergesort(array, 0, 7);
	for (int i = 0; i < 8; i++) {
		cout << array[i] << " ";
	}
}