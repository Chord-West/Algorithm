#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


vector<int> solution(vector<string> &s) {
	vector<int> re;
	for (int i = 0; i < s.size()-1; i++)
	{
		for (int j = 0; j < s[0].length(); j++) {
			if (s[i][j] == s[i+1][j]) {

			}
		}
	}
	return  re;
}

int main() {
	vector<string> a = { "abc","bca","dbe" };
	vector<int> ans;
	ans=solution(a);

}
