/*삽입정렬을 구현하시오.표준 출력으로부터의 입력은 다음과 같다.
첫번째 행에 데이터의 갯수 n 이 2 와 1000 사이의 정수로 주어진다.
두번째 행부터 n + 1 번째 행에 정수와 영어단어(영어 단어는 satellite data)의 쌍이 공백으로 구분되어 주어진다.
이 n 개의 데이터들을 삽입정렬을 사용하여 정수의 오름차순으로 정렬하여 표준 출력에 정수와 영어 단어의 쌍을 출력하라.*/
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <fstream>
using namespace std;

int main(void) {
    int n;
    ifstream cin;
    cin.open("input.txt");
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
    // output 
    for (int i = 0; i < n; i++) {
        cout << v[i].first << ' ' << v[i].second << endl;
    }

}