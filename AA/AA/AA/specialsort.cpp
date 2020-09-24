#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input2.txt");
	int n,num,i,j;
	int count = 0; 
	vector<int> arr;
	
	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> num;
		arr.push_back(num);
	}
	for (i = 0; i < n; i++) {
		if (arr[i] < 0) {
			for (j = i; j >count; j--) {
					int tmp = arr[j];
					arr[j] = arr[j - 1];
					arr[j -1] = tmp;
			}
			count++;
		}
	}
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
}