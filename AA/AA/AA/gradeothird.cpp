#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input2.txt");
	int n,num,i,j,index,tmp;
	vector<int> arr;
	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> num;
		arr.push_back(num);
	}
	for (i = 0; i < arr.size(); i++) {
		index = i;
		for (j = i + 1; j < arr.size(); j++) {
			if (arr[index] <= arr[j]) index = j;
		}
		tmp = arr[index];
		arr[index] = arr[i];
		arr[i] = tmp;
	}
	int grade = arr[0];
	int order = 1;
	for (i = 1; i < n; i++) {
		if (arr[i] == grade) continue;
		else {
			grade = arr[i];
			order++;
			if (order == 3) break;
		}
	}
	cout << grade;
}