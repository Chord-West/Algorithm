#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input2.txt");
	int n,num,i;
	int idx, tmp;
	cin >> n;
	vector<int> arr;
	for ( i = 0; i < n; i++) {
		cin >> num;
		arr.push_back(num);
	}
	for ( i = 0; i < arr.size(); i++) {
		int idx = i;
		for (int j = i+1; j < arr.size(); j++) {
			if (arr[idx] > arr[j]) 
				idx = j;
		}
		tmp = arr[idx];
		arr[idx] = arr[i];
		arr[i] = tmp;
	}
	for (i = 0; i < arr.size(); i++) {
		cout << arr[i] << " ";
	}
}