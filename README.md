# Algorithm
#### Sort

##### - InsertionSort

------

```	c++
#include <iostream>
using namespace std;
int main() {
	int array[10] = { 1,10,5,8,7,6,4,3,2,9 };
	int j,temp;
	for (int i = 1; i < 9; i++) {
		j = i;
		while (j > 0 && array[j-1] > array[j ]) {
			temp = array[j-1];
			array[j-1] = array[j];
			array[j ] = temp;
			j--;
		}
	}
	for (int i = 0; i < 10; i++) cout << array[i] << " ";

}
```



- Quiz

  ```c++
  #include <iostream>
  #include <vector>
  using namespace std;
  int main(void) {
      pair<int,string> tmp;
      vector<pair<int, string> > v;
      cin >> n;
      for (int i = 0; i < n; i++) {
          int d;
          string s;
          cin >> d >> s;
          v.push_back(pair<int, string>(d, s));
      }
      // insertion sort
      for (int i = 0; i < v.size(); i++) {
          int key = i;
          while (key > 0 && v[key-1].first > v[key ].first) {
              tmp = v[key-1];
              v[key -1]=v[key];
              v[key] = tmp;
              key--;
          }
      }
  }
  ```

  

##### - MergeSort

---

```C++
#include <iostream>
#include <vector>
using namespace std;
int n = 10;
vector<int> sorted(n);
void merge(vector<int>& a, int m, int middle, int n) {
	int i = m; //2개중 첫번째
	int j = middle + 1; // 2개중 두번째
	int k = m; // 합친배열의 첫번째
	//작은 순서대로 배열에 삽입
	while (i <= middle && j <= n) {//작은값을 k에 넣어줌
		if (a[i] <= a[j]) {
			sorted[k] = a[i];
			i++;
		}else {
			sorted[k] = a[j];
			j++;
		}
		k++;// 다음 원소에 값을 받을 수 있도록함
	}if (i > middle){  //i 가 먼저 배열에 도달했을경우
		for (int t = j; t <= n; t++) {
			sorted[k] = a[t];
			k++;
		}
	}else {
		for (int t = i; t <= middle; t++) {
			sorted[k] = a[t];
			k++;
		}
	}//정렬된 배열을 삽입
	for (int t = m; t <= n; t++) a[t] = sorted[t];
}
void mergesort(vector<int>& a, int p, int r) {
	if (p < r) {
		int middle = (p + r) / 2;
		mergesort(a, p, middle);
		mergesort(a, middle + 1, r);
		merge(a, p, middle, r);
	}
}
int main() {
	vector<int> v = { 1, 10, 5, 8, 7, 6, 4, 3, 2, 9 };
	mergesort(v, 0, n - 1);
	for (int i = 0; i < sorted.size(); i++)
		cout << sorted[i] << " ";
}
```

- Quiz (Maximum Subarray)

  ```c++
  #include <iostream> 
  #include <climits> 
  #include <vector>
  using namespace std;
  int max(int a, int b) { return (a > b) ? a : b; }
  int max(int a, int b, int c) { return max(max(a, b), c); }
  int maxCrossingSum(vector<int>& arr ,int l, int m, int h){
      int sum = 0;
      int left_sum = INT_MIN;
      for (int i = m; i >= l; i--){
          sum = sum + arr[i];
          if (sum > left_sum) left_sum = sum;
      }
      sum = 0;
      int right_sum = INT_MIN;
      for (int i = m + 1; i <= h; i++){
          sum = sum + arr[i];
          if (sum > right_sum)right_sum = sum;
      }
      return max(left_sum + right_sum, left_sum, right_sum);
  }
  int maxSubArraySum(vector<int>& arr, int l, int h){
      if (l == h) return arr[l];
      int m = (l + h) / 2;
      return max(maxSubArraySum(arr, l, m),maxSubArraySum(arr, m + 1, h),maxCrossingSum(arr, l, m, h));
  }
  
  int main()
  {
      vector<int> arr = { 2, 3, 4, 5, 7 };
      int max_sum = maxSubArraySum(arr, 0, arr.size() - 1);
      cout << max_sum;
      return 0;
  }
  ```

  

##### - HeapSort

------

```c++
#include <iostream>
#include <vector>
using namespace std;
int number = 9;
vector<int> heap = { 7,6,5,8,3,5,9,1,6 }; 
int main() {
	ios_base::sync_with_stdio(false);	// 먼저 전체 트리 구조를 max heap 구조로 바꿈
	for (int i = 1; i < number; i++) {
		int child = i;
		do {
			int root = (child - 1) / 2;
			if (heap[root] < heap[child]) {
				int tmp = heap[root];
				heap[root] = heap[child];
				heap[child] = tmp;
			}
			child = root;
		} while (child != 0);
	}
	// 크기를 줄여가며 반복적으로 힙을 구성 ( 정렬 )
	for (int i = number - 1; i >= 0; i--) {
		int tmp = heap[0];
		heap[0] = heap[i];
		heap[i] = tmp;
		int root = 0;
		int child = 1;
		do {
			child = 2 * root + 1; //자식 중에 더 큰 값을 찾기
			if (child < i - 1&&heap[child] < heap[child + 1] ) {
				child++; 
			}
			//루트보다 자식이 더 크다면 교환
			if (child < i&&heap[root] < heap[child] ) {
				int tmp = heap[root];
				heap[root] = heap[child];
				heap[child] = tmp;
			}
			root = child;
		}while(child < i);
	}
	for (int i = 0; i < number; i++)
		cout << heap[i] << " ";
}
```



##### - QuickSort

------

```c++
#include <iostream>
#include <vector>
using namespace std;
void quicksort(vector<int>& data, int start, int end) {
	if (start >= end) return; // 원소가 1개인경우
	int key = start; //키는 첫 번째 원소
	int i = start + 1; //왼쪽 출발지점
	int j = end; //오른쪽 출발지점
	int tmp;
	while (i <= j) {// 엇갈릴 때까지 반복
		while (i <=end&& data[i] <= data[key]) i++; // 키 값보다 큰 값을 만날 때 까지
		while (j>start&&data[j] >= data[key])  j--;
		if (i > j) { //현재 엇갈린 상태면 키 값과 교체
			tmp = data[j];
			data[j] = data[key];
			data[key] = tmp;
		}
		else {
			tmp = data[j];
			data[j] = data[i];
			data[i] = tmp;
		}
		quicksort(data, start, j - 1);
		quicksort(data, j + 1, end);
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	vector<int> arr = { 1,10,5,8,7,6,4,3,2,9 };
	quicksort(arr, 0, arr.size() - 1);
	for (int i = 0; i < arr.size(); i++) cout << arr[i] << " ";
	return 0;
}
```



##### - CoutingSort

---

```c++
#include <iostream>
#include <vector>
using namespace std;
// 범위 조건이 있을때 사용 가능 ex ) 5이하의 수 정렬
int main() {
	vector<int> arr = { 2,5,3,0,2,3,0,3 };
	vector<int> ans(arr.size()); // 정렬될 배열
	vector<int> count(5+1, 0);
	for (int i = 0; i <arr.size(); i++) {
		count[arr[i]]++;
	}
	for (int i = 1; i < count.size(); i++) {
		count[i] = count[i] + count[i - 1];
	}
	for (int i = arr.size() - 1; i > 0;i-- ) {
		ans[count[arr[i]]-1] = arr[i];
		count[arr[i]]--;
	}
	for (int i = 0; i < arr.size(); i++) {
		cout << ans[i] << " ";
	}
}
```

- Quiz (Radixsort)

  ```c++
  #include <iostream>
  #include <vector>
  #include <string>
  using namespace std;
  
  vector<pair<int, string> > v;
  int n;
  int digit16(int v, int d) {
      // 양의 정수 v 의 16진수 d 번째 숫자를 반환하는 함수
      // 예를 들어 v 의 값이 78320238 (= 0x04ab126e) 이고 d 가 1 이라면 6 을 반환
      // 예를 들어 v 의 값이 78320238 (= 0x04ab126e) 이고 d 가 4 라면 11 (= 0xb) 을 반환
      v = v >> d * 4;
      return v & 0xf;
  }
  void countingSort16(vector<pair<int, string> >& v, int d) {
      vector<pair<int, string> > tmp(v.size());
      vector<int> c(16, 0);
      vector<int> a(n); //16진수 input
      for (int i = 0; i < n; i++) {
          a[i] = digit16(v[i].first, d); //input
          c[a[i]]++;
      }
      for (int i = 1; i < c.size(); i++)  c[i] = c[i] + c[i - 1];
      
      for (int i = a.size() - 1; i >= 0; i--) {
          tmp[c[a[i]] - 1] = v[i];
          c[a[i]] = c[a[i]] - 1;
      }
      v = tmp;
  }
  int main(void) {
      cin >> n;
      for (int i = 0; i < n; i++) {
          int d;
          string s;
          cin >> d >> s;
          v.push_back(pair<int, string>(d, s));
      }
      //radixsort
      for (int d = 0; d < 8; d++) countingSort16(v, d);
      
      for (int i = 0; i < n; i++)  cout << v[i].first << ' ' << v[i].second << endl;
      return 0;
  }
  ```

  

