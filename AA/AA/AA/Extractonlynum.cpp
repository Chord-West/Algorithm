#include<iostream>
#include<fstream>
#include<vector>
#include <string>
#include<cmath>


using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin;
	cin.open("input.txt");
	int sum = 0;
	int answer = 0;
	string a;
	vector<int> num;
	cin >> a;
	for (int i = 0; i <= a.length(); i++) 
		if ((a[i] - 48) >= 0 && (a[i] - 48) <= 9) 
			sum = sum * 10 + (a[i] - 48);
	
	for (int i = 1; i <= sum; i++) 
		if (sum % i == 0) answer += 1;
	

	cout << sum << endl << answer;

}