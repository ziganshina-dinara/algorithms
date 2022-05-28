#include <iostream>
#include <set>

using namespace std;

int most_frequent_sequence_element() {
    multiset <int> s;
    set <int> unique_s;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        s.insert(x);
        unique_s.insert(x);
    }
    int max_cnt = 0;
    int element_with_max_cnt = -5;
    for (auto element : unique_s){
        int cnt = 0;
        for (auto now = s.lower_bound(element); now != s.upper_bound( element); now++) {
        cnt++;
        }
        if (cnt >= max_cnt) {
            max_cnt = cnt;
            element_with_max_cnt =  element;
        }
    }
    cout <<  element_with_max_cnt;
    return 0;
}

int main() {
    most_frequent_sequence_element();
    return 0;
}

