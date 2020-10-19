#include <iostream>
#include <vector>
using namespace std;
// 범위 조건이 있을때 사용 가능 ex ) 5이하의 수 정렬
int main() {
	vector<int> arr = { 2,5,3,0,2,3,0,3 };
	vector<int> ans(arr.size()); // 정렬될 배열
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