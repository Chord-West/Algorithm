#include <iostream>
#include <vector>

using namespace std;



void quicksort(vector<int>& data, int start, int end) {
	if (start >= end) return; // ���Ұ� 1���ΰ��
	int key = start; //Ű�� ù ��° ����
	int i = start + 1; //���� �������
	int j = end; //������ �������
	int tmp;
	while (i <= j) {// ������ ������ �ݺ�
		while (i <=end&& data[i] <= data[key]) i++; // Ű ������ ū ���� ���� �� ����
		while (j>start&&data[j] >= data[key])  j--;
		if (i > j) { //���� ������ ���¸� Ű ���� ��ü
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