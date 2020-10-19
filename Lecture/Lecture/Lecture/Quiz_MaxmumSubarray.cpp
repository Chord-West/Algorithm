/*배열에서 연속된 부분 배여의 합이 최대값이 되는 부분 배열을
Maximum subarray 라고 한다. -100과 100 사이의 정수들을 원소로 가지는 배열에서
maximum subarray를 찾아 그 원소들의 합을 반환하는 함수를 구현하라 */

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
