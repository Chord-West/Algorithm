#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<pair<int, string> > v;
int n;
int digit16(int v, int d) {
    // ���� ���� v �� 16���� d ��° ���ڸ� ��ȯ�ϴ� �Լ�
    // ���� ��� v �� ���� 78320238 (= 0x04ab126e) �̰� d �� 1 �̶�� 6 �� ��ȯ
    // ���� ��� v �� ���� 78320238 (= 0x04ab126e) �̰� d �� 4 ��� 11 (= 0xb) �� ��ȯ
    v = v >> d * 4;
    return v & 0xf;
}
void countingSort16(vector<pair<int, string> >& v, int d) {
    vector<pair<int, string> > tmp(v.size());
    vector<int> c(16, 0);
    vector<int> a(n); //16���� input
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
