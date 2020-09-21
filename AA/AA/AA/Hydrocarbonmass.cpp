#include <iostream>
#include <fstream>
#include <vector>
#include<string>

using namespace std;

int main() {
	//ifstream cin;
	//cin.open("input.txt");
	string ep;
	cin >> ep;
	int c = 12;
	int h = 1;
	int cnum = 0;
	int hnum = 0;
	int index = 1;
	for (int i = 1; i < ep.length(); i++) {
		if (ep[i] == 'H') {
			index = i + 1;
			break;
		}
		if (ep[i] - 48 >=0 && ep[i]-48 < 10) 
			cnum = cnum * 10 + ep[i] - 48;
	}
	for (int i = index; i < ep.length(); i++) {
		if (ep[i] - 48 >= 0 && ep[i]-48 < 10) 
			hnum = hnum * 10 + ep[i] - 48;
	}
	if (cnum == 0)
		cnum = 1;
	if (hnum == 0)
		hnum = 1;
	cout << c * cnum + h * hnum;
 }