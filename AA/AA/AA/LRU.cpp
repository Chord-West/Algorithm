#include <iostream>
#include <vector>
#include <fstream>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input2.txt");
	int s, n,num;
	cin >> s >> n;
	vector<int> c(s);
	for (int i = 0; i < n; i++) {
		cin >> num;
		int pos = -1;
		for (int j = 0; j < s; j++) {
			if (c[j] == num) 
				pos = j;
		}
		if (pos == -1) //Miss ³µÀ»‹š
		{
			for (int j = s - 1; j >= 1; j--)  c[j] = c[j - 1];
		}
		else {
			for (int j = pos; j >=1; j--)  c[j] = c[j - 1];
		}
		c[0] = num;
	}
	for (int i = 0; i < s; i++) {
		cout << c[i] << " ";
	}
}