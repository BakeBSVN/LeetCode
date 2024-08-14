#include <bits/stdc++.h>
using namespace std;
#define ll long long int
void Input(){
    FILE* fp = fopen("A.inp", "r");
    if (fp != NULL) {
        freopen("A.inp", "r", stdin);
        freopen("A.out", "w", stdout);
        fclose(fp);
    }
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int Solve(){

  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
         int count = 0;
    ListNode *p = head;
    while(p != NULL){
        count++;
        p = p->next;
    }
    if (count == n) { // Xóa node đầu tiên
        ListNode *newHead = head->next;
        head->next = NULL;
        delete head;
        return newHead;
    }
    int k = count - n;
    ListNode *pre = head;
    ListNode *del = head->next;
    while(k > 1){ // Tìm node trước node cần xóa
        pre = pre->next;
        del = del->next;
        k--;
    }
    pre->next = del->next;
    del->next = NULL;
    delete del;
    return head;
    }
};   //Your code here
}


int main(){
    Input();
    Solve();
}
