#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

string solution(vector<string> participant, vector<string> completion);

int main() {
	ios_base::sync_with_stdio(false);
	vector<string> p = {"leo","kiki","eden"};
	vector<string>	c = {"eden","kiki"};

	string answer = solution(p, c);
	cout << answer << endl;
}

string solution(vector<string> participant, vector<string> completion)
{

}