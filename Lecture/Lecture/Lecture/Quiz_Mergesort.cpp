/*
Mergesort를 구현하시오. 표준 출력으로부터의 입력은 다음과 같다. 첫번째 행에 데이터의 갯수 n 이 2 와 1000 사이의 정수로 주어진다.
두번째 행부터 n+1 번째 행에 정수와 영어단어의 쌍이 공백으로 구분되어 주어진다.
이 n개의 데이터들을 내림차순으로 stable하게 정렬하여 표준 출력에 정수와 영어 단어의 쌍을 출력하라
*/



#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <climits>
using namespace std;

void mergesort(vector<pair<int, string> >& v, int p, int r);
void merge(vector<pair<int, string> >& v, int p, int middle,int r);
vector<pair<int, string> > sorted(1001);

int main(void) {
    int n;
    vector<pair<int, string> > v;
    int max = INT_MAX;
    int min = INT_MIN;

    cin >> n;

    for (int i = 0; i < n; i++) {
        int d;
        string s;
        cin >> d >> s;
        v.push_back(pair<int, string>(d, s));
    }

    // merge sort
    mergesort(v, 0, v.size() - 1);

    for (int i = 0; i < n; i++) {
        cout << v[i].first << ' ' << v[i].second << endl;
    }

    return 0;
}

void mergesort(vector<pair<int, string> >& v, int p, int r) {
    if (p < r) {
        int middle = (p + r) / 2;
        mergesort(v, p, middle);
        mergesort(v, middle+1, r);
        merge(v, p, middle, r);
    }
}

void merge(vector<pair<int, string> >& v, int p, int middle, int r) {
    int i = p;
    int j = middle + 1;
    int k = p;

    while (i <= middle && j <= r) {
        if (v[i].first >= v[j].first) {
            sorted[k] = v[i];
            i++;
        }
        else {
            sorted[k] = v[j];
            j++;
        }
        k++;
    }
    if (i > middle) {
        for (int t = j; t <= r; t++) {
            sorted[k] = v[t];
            k++;
        }
    }
    else {
        for (int t = i; t <= middle; t++) {
            sorted[k] = v[t];
            k++;
        }
    }
    for (int t = p; t <= r; t++) {
        v[t]=sorted[t];
    }
}