#include <iostream>
#include <vector>
#include <fstream>

using namespace std;


//12 11 10 9 8 7 5 6 4 3 2 1, 3 2 2 5 2 2 2 2 5 3 2 2 2 2
int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	int n;
	int two = 0;
	int five = 0;
	int min;
	cin >> n;
	for (int i = 2; i <= n; i++) {
		int num = i;
		int j = 2;
		while (num != 1) {
			if (num % j == 0) {
				if (j == 2)  two++;
				else if (j == 5)  five++;
				num /= j;
			}
			else j++;
		}

	}
	if (two > five) {
		min = five;
	}
	else
		min = two;

	cout << min;
}