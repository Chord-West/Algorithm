#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//ifstream cin;
	char a[20];
	int age=0;
	char s;
	//cin.open("input.txt");
	cin >> a;
	if (a[7]=='1'|| a[7]=='2') age = 100 - ((a[0]-48) * 10 + (a[1]-48)) + 20;
	else  age = 20 - ((a[0] - 48) * 10 + (a[1] - 48));
	if (a[7] == '1' || a[7] == '3')	s = 'M';
	else s = 'W';
	cout << age<<" "<<s;
	return 0;
}