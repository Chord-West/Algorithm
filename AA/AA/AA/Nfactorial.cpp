#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	int n;
	cin >> n;
	vector<bool> check(n+1, false);
	vector<int> prime;
	vector<int> counter;
	//5*4*3*2*1
	for (int i = 2; i <= n; i++) {
		int num = i;
		if (check[i] == false) {
			prime.push_back(i);// 2,3,5,7
			counter.push_back(1);
			for (int j = i + i; j <= n; j += i) {
				check[j] = true;
			}
		}
		else if (check[i] = true) {
			int k = 0;
			while (num > 1) {
				if (num%prime[k]==0) {
					counter[k]++;
					num = num / prime[k];
				}
				else {
					k++;
				}
			}
		}
	}
	cout << n << "! = ";
	for (int i = 0; i < counter.size(); i++) {
		cout << counter[i] << " ";
	}

}