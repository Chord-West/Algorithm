/*�迭���� ���ӵ� �κ� �迩�� ���� �ִ밪�� �Ǵ� �κ� �迭��
Maximum subarray ��� �Ѵ�. -100�� 100 ������ �������� ���ҷ� ������ �迭����
maximum subarray�� ã�� �� ���ҵ��� ���� ��ȯ�ϴ� �Լ��� �����϶� */

#include <vector>
#include <climits>
#include <iostream>
using namespace std;
int max(int a, int b) { return (a > b) ? a : b; }
int max(int a, int b, int c) { return max(max(a, b), c); }
int solution(vector<int>& param0) {
	int answer = maximumSubarray(param0, 0, param0.size() - 1);
	return answer;
}
int maximumSubarray(vector<int>& v, int low, int high) {
	if (low == high) return v[i];
	int mid = (low + high) / 2;
	return 	max(maximumSubarray(v, low, mid), maximumSubarray(v, mid + 1, high), crossSubarray(v, low, mid, high));
}

int  crossSubarray(vector<int>& v, int low, int mid, int higih) {
	int sum = 0;
	int lr_sum = 0;
	int left_sum = INT_MIN;
	int right_sum = INT_MAX;

	for (int i = mid; i >= low; i--) {
		sum += v[i];
		if (sum > left_sum) left_sum = sum;
	}
	sum = 0;
	for (int i = mid + 1; i <= higih; i++) {
		sum += v[i];
		if (sum > left_sum) left_sum = sum;
	}
	lr_sum = left_sum + right_sum;
	return max(lr_sum, left_sum, right_sum);
}

int main() {
	vector<int> v = { 13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7 };
	solution(v);

}