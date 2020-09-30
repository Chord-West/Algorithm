#include <iostream>
#include <vector>

using namespace std;

int solution(int n, vector<int> stations, int w)
{
    int answer = 3;
    vector<int> apt(n+1);
    for (int i = 1; i <= n; i++) apt[i] = i;
    while (stations.size() != 0) {
        int num = stations.back();
        stations.pop_back(); //1°³¾¿ »©±â
        for (int i = num - w; i < num + w; i++) {
            if (i > n || i < 1)
                continue;
            else apt[i] = 0;
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << apt[i] << " ";
    }

    return answer;
}

int main() {
    int n = 11, w = 1;
    vector<int> v = {4,11};
    cout << solution(n, v, w);
}