#include <iostream>
#include <vector>
using namespace std;
// ���� ������ ������ ��� ���� ex ) 5������ �� ����
int main() {
	vector<int> arr = { 2,5,3,0,2,3,0,3 };
	vector<int> ans(arr.size()); // ���ĵ� �迭
	vector<int> count(5+1, 0);
	for (int i = 0; i <arr.size(); i++) {
		count[arr[i]]++;
	}
	for (int i = 1; i < count.size(); i++) {
		count[i] = count[i] + count[i - 1];
	}
	for (int i = arr.size() - 1; i > 0;i-- ) {
		ans[count[arr[i]]-1] = arr[i];
		count[arr[i]]--;
	}
	for (int i = 0; i < arr.size(); i++) {
		cout << ans[i] << " ";
	}
}