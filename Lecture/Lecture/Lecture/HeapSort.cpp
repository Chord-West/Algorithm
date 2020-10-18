#include <iostream>
#include <vector>

using namespace std;

int number = 9;
vector<int> heap = { 7,6,5,8,3,5,9,1,6 }; 

int main() {
	ios_base::sync_with_stdio(false);
	// ���� ��ü Ʈ�� ������ max heap ������ �ٲ�
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
	// ũ�⸦ �ٿ����� �ݺ������� ���� ���� ( ���� )
	for (int i = number - 1; i >= 0; i--) {
		int tmp = heap[0];
		heap[0] = heap[i];
		heap[i] = tmp;
		int root = 0;
		int child = 1;
		do {
			child = 2 * root + 1; //�ڽ� �߿� �� ū ���� ã��
			if (child < i - 1&&heap[child] < heap[child + 1] ) {
				child++; 
			}
			//��Ʈ���� �ڽ��� �� ũ�ٸ� ��ȯ
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