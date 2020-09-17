#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	vector<int> tmp;
	
	int n, k;
	int num;
	int sum = 0;;
	int max = -2147000;
	int index = 0;
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> num;
		tmp.push_back(num);
	}
	for (int i = 0; i < k; i++) sum+= tmp[i]; //�ʱⰪ
	if (sum > max) max = sum;
	
	for (int i = k; i <= n-1; i++) {
		sum +=tmp[i];
		sum -= tmp[index];
		index++;
		if (sum > max) {
			max = sum;
		}
	}
	cout << max;
}