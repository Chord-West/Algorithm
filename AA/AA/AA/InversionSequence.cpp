#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin;
	cin.open("input2.txt");
	int n,i,j,num,pos;
	cin >> n;
	vector<int> is(n + 1), os(n + 1);
	for (i = 1; i <= n; i++) {
		cin >> num;
		is[i] = num;
	}
	for (i = n; i >= 1; i--) {
		pos = i;
		for (j = 1; j <= is[i]; j++) {
			os[pos] = os[pos + 1];
			pos++;
		}
		os[pos] = i;
	}
	for (i = 1; i <= n; i++) {
		cout << os[i] << " ";
	}
}