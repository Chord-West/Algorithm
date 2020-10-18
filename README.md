# Algorithm
for algorithm study

##### HeapSort

------

```c++
#include <iostream>
#include <vector>
using namespace std;
int number = 9;
vector<int> heap = { 7,6,5,8,3,5,9,1,6 }; 
int main() {
	ios_base::sync_with_stdio(false);	// 먼저 전체 트리 구조를 max heap 구조로 바꿈
	for (int i = 1; i < number; i++) {
		int child = i;
		do {
			int root = (child - 1) / 2;
			if (heap[root] < heap[child]) {
				int tmp = heap[root];
				heap[root] = heap[child];
				heap[child] = tmp;
			}
			child = root;
		} while (child != 0);
	}
	// 크기를 줄여가며 반복적으로 힙을 구성 ( 정렬 )
	for (int i = number - 1; i >= 0; i--) {
		int tmp = heap[0];
		heap[0] = heap[i];
		heap[i] = tmp;
		int root = 0;
		int child = 1;
		do {
			child = 2 * root + 1; //자식 중에 더 큰 값을 찾기
			if (child < i - 1&&heap[child] < heap[child + 1] ) {
				child++; 
			}
			//루트보다 자식이 더 크다면 교환
			if (child < i&&heap[root] < heap[child] ) {
				int tmp = heap[root];
				heap[root] = heap[child];
				heap[child] = tmp;
			}
			root = child;
		}while(child < i);
	}
	for (int i = 0; i < number; i++)
		cout << heap[i] << " ";
}
```



###### QuickSort

------

```c++
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
	for (int i = 0; i < arr.size(); i++) cout << arr[i] << " ";
	return 0;
}
```



