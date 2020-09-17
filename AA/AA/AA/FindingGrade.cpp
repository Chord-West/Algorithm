#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	//fstream cin;
	//cin.open("input.txt");
	int n;
	cin >> n;
	int num;
	vector<int> arr;
	vector<int> check(n,1);
	for (int i = 0; i < n; i++) {
		cin>>num;
		arr.push_back(num);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i] > arr[j]) {
				check[j]++;
			}
		}
	}
	for (int i = 0; i < check.size(); i++)
		cout << check[i]<<" ";
}