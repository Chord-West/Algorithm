#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//ifstream cin;
	//cin.open("input.txt");
	
	string b;
	cin >> b;
	int cnt = 0;

	for (int i = 0; i < b.length(); i++) {
		if (b[i] == '(')  cnt++;
		else  cnt--;
		if (cnt == -1)
			break;
		
	}
	
	if (cnt == 0) cout << "YES";
	else cout << "NO";

}