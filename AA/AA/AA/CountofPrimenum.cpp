#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int n;
	int answer = 0;
	cin >> n;
	vector<bool> check(n+1);
	for (int i = 2; i <= n; i++) {
		if (!check[i]) {
			answer++;
			for (int j = i + i; j <= n; j += i) check[j] = true;
		}
	}

	cout << answer;
}