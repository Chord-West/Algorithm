#include <iostream>
#include <vector>

using namespace std;



void quicksort(vector<int>& data, int start, int end) {
	if (start >= end) return; // 원소가 1개인경우
	int key = start; //키는 첫 번째 원소
	int i = start + 1; //왼쪽 출발지점
	int j = end; //오른쪽 출발지점
	int tmp;
	while (i <= j) {// 엇갈릴 때까지 반복
		while (i <=end&& data[i] <= data[key]) i++; // 키 값보다 큰 값을 만날 때 까지
		while (j>start&&data[j] >= data[key])  j--;
		if (i > j) { //현재 엇갈린 상태면 키 값과 교체
			tmp = data[j];
			data[j] = data[key];
			data[key] = tmp;
		}
		else {
			tmp = data[j];
			data[j] = data[i];
			data[i] = tmp;
		}
		quicksort(data, start, j - 1);
		quicksort(data, j + 1, end);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	vector<int> arr = { 1,10,5,8,7,6,4,3,2,9 };
	quicksort(arr, 0, arr.size() - 1);
	for (int i = 0; i < arr.size(); i++) {
		cout << arr[i] << " ";
	}
	return 0;
}