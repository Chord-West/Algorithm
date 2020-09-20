#include <iostream>
#include <vector>

using namespace std;


int number = 8;
vector<int> sorted(8);


void merge(int a[], int m, int middle, int n) {
	int i = m; //2개중 첫번째
	int j = middle + 1; // 2개중 두번째
	int k = m; // 합친배열의 첫번째
	//작은 순서대로 배열에 삽입
	while (i <= middle && j <= n) {
		//작은값을 k에 넣어줌
		if (a[i] >= a[j]) {
			sorted[k] = a[i];
			i++;
		}
		else {
			sorted[k] = a[j];
			j++;
		}
		k++;// 다음 원소에 값을 받을 수 있도록함
	}
	if (i > middle)  //i 가 먼저 배열에 도달했을경우
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
	//정렬된 배열을 삽입
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