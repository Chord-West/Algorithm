/*���������� �����Ͻÿ�.ǥ�� ������κ����� �Է��� ������ ����.
ù��° �࿡ �������� ���� n �� 2 �� 1000 ������ ������ �־�����.
�ι�° ����� n + 1 ��° �࿡ ������ ����ܾ�(���� �ܾ�� satellite data)�� ���� �������� ���еǾ� �־�����.
�� n ���� �����͵��� ���������� ����Ͽ� ������ ������������ �����Ͽ� ǥ�� ��¿� ������ ���� �ܾ��� ���� ����϶�.*/
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