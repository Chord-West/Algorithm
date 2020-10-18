#include <string>
#include <vector>
#include <climits>
#include <iostream>


using namespace std;

int solution(vector<int> param0) {
    int answer = 0;
    int max = -21470000;
    int sum = 0;
    for (int i = 0; i < param0.size(); i++) {
        sum += param0[i];
        if (sum < param0[i])
            sum = param0[i];
        if (sum > max) {
            max = sum;
        }
    }
    answer = max;
    return answer;
}


int main() {
    vector<int> arr = { -72,94,-4 };
    cout << solution(arr);
}
