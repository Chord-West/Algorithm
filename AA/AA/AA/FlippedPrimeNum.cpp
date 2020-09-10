#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
const int MAX = 100000;
int reverse(int x);
bool isPrime(int x);
vector<bool> prime(MAX + 1); 

int main() {
	ios_base::sync_with_stdio(false);
	//ifstream cin;
	int t,num;
	prime[1] = true;
	for (int i = 2; i < MAX; i++) {
		if (!prime[i]) { // false 면 소수
			for (int j = i+i; ; j += i) {
				if (j > MAX) break;
				prime[j] = true;
			}
		}
	}
	//cin.open("input.txt");
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> num;
		int r_num = reverse(num);
		if (isPrime(r_num)) {
			cout << r_num << " ";
		}
	}

}

int reverse(int x) {
	int sum = 0;
	while (x > 0) {
		int r=x % 10;
		sum =sum*10+ r;
		x /= 10;
	}
	return sum;
}

bool isPrime(int x) {
	if (!prime[x]) return true;//소수
	else return false;
}