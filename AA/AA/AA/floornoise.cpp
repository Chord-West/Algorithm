#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	int n, lim,warn;
	bool check = false;
	int max=0;
	int answer = -1;
	cin >> n >> lim;
	for (int i = 0; i < n; i++) {
		cin >> warn;
		if (lim <warn) {
			max++;
			check = true;
		}
		else {
			max = 0;
			check = false;
		}
		if (check&&answer<max) 
			answer = max;
	}
	cout << answer;
}