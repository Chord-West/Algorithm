#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input2.txt");
	vector<int> arr;
	int n,num,i,j;
	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> num;
		arr.push_back(num);
	}
	for (i = 0; i < arr.size(); i++) {
		for (j = 0; j < arr.size()-i-1; j++) {
			if (arr[j] > arr[j + 1]) {
				int tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
		}
	}
	for (i = 0; i < arr.size(); i++) 
		cout << arr[i] << " ";
}