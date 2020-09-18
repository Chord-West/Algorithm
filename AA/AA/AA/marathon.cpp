#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	vector<int> player;
	int n,i;
	int num;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		player.push_back(num);
	}
	cout << "1 ";
	for (i = 1; i < player.size(); i++) {
		int cnt = 0;
		for (int j = i - 1; j > -1; j--) {
			if (player[j] >= player[i]) cnt++;
		}
		cout << cnt + 1 << " ";
	}
}