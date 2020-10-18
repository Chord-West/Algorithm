#include <iostream>
#include <vector>

using namespace std;

vector<int> heap = { 7,6,5,8,3,5,9,1,6 }; 

int main() {
	ios_base::sync_with_stdio(false);
	for (int i = 1; i < heap.size(); i++) {
		int c = i; // ÀÚ½Ä
		
		while (c != 0) {
			int root =(c - 1)/2 ;
			if (heap[root] < heap[c]) {
				int tmp = heap[root];
				heap[root] = heap[c];
				heap[c] = tmp;
			}
			c = root;
		}
	}
	for (int i = heap.size() - 1; i >= 0;i--) {
		int tmp = heap[0];
		heap[0] = heap[i];
		heap[i] = tmp;
		int root = 0;
		int c = 1;
		while (c < i) {
			c = 2 * root + 1;
			if (c < i - 1 && heap[c] < heap[c + 1]) c++;
			if (c < i && heap[root] < heap[c]) {
				int tmp = heap[root];
				heap[root] = heap[c];
				heap[c] = tmp;
			}
			root = c;
		}
	}
	for (int i = 0; i < heap.size(); i++) {
		cout << heap[i] << " ";
	}
}