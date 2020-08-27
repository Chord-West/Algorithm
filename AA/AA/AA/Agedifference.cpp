#include <iostream>
#include <fstream>


using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin;
	cin.open("input.txt");
	int n,num;
	int max = 0;
	int min = 101;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		if (num > max) {
			max = num;
		}
		if(num<min){
			min = num;
		}
	}
	cout << max - min;
	return 0;
}