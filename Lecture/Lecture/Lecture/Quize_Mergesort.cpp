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