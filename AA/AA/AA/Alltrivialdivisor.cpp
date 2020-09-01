#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);

	int num;
	int count = 1;
	cin >> num;
	vector<int> answer(num+1);
	for (int i = 1; i <= num; i++) {
		for (int j =i; j <= num; j=j+i) {
			if ( j%i == 0) 
				answer[j]++;			
		}
		cout<<answer[i]<<" ";
	}
	
}