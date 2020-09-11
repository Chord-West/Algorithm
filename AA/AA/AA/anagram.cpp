#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	fstream cin;
	cin.open("input.txt");
	string str1;
	string str2;
	cin >> str1>>str2;
	sort( str1.begin(), str1.end());
	sort(str2.begin(), str2.end());
	cout << str1 << " " << str2;
	if (str1 == str2)
		cout << "YES";
	else
		cout << "NO";
}