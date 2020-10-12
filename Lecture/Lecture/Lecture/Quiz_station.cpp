#include <iostream>
#include <vector>

using namespace std;

int solution(int n, vector<int> stations, int w)
{
	int answer = 0;
	int start = 0;
	int dis = w * 2 + 1;
	for (int i = 0; i < stations.size(); i++) {
		int lt = stations[i] - 1 - w;
		int rt = stations[i] - 1 + w;
		if (start >= lt && start <= rt) {
			start = rt + 1;
			continue;
		}

		int div = (lt - start) / dis;
		int rest = (lt - start) % dis;
		if (rest > 0) {
			div += 1;
		}
		answer += div;

		start = rt + 1;
	}
	if (start < n) {
		int div = (n - start) / dis;
		int rest = (n - start) % dis;
		if (rest > 0)
			div += 1;
		answer += div;
	}

	return answer;
}

int main() {
    int n = 16, w = 2;
    vector<int> v = {9};
    cout << solution(n, v, w);
}