#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;
//이기면 3점 지면 0점 비기면 1점 // 10번라운드
//승점이 같은경우 마지막에 이긴사람을 게임의 승자, 모두비기면 모두비김

int main() {
	ios_base::sync_with_stdio(false);
	//ifstream cin;
	//cin.open("input.txt");
	int n,num;
	int A_index = 0;
	int B_index=0;
	vector<int> a, b;
	int A = 0;
	int B = 0;
	for (int i = 0; i < 10; i++) {
		cin >> num;
		a.push_back(num);
	}
	for (int i = 0; i < 10; i++) {
		cin >> num;
		b.push_back(num);
	}
	for (int i = 0; i < 10; i++) {
		if (a[i] > b[i]) {
			A += 3;
			A_index = i;
		}
		else if (a[i] < b[i]) {
			B += 3;
			B_index = i;
		}
		else {
			A += 1;
			B += 1;

		}
	}
	cout << A << " " << B << endl;
	if (A > B) cout << "A";
	else if (A < B) cout << "B";
	else {
		if (A_index > B_index) cout << "A";
		else if (A_index < B_index) cout << "B";
		else cout << "D";
	}
}