#include <bits/stdc++.h>
using namespace std;
#define ll long long int

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* p = NULL;
        ListNode* q = NULL;
        while (head){
            p = head->next;
            head->next = q;
            q = head;
            head = p;
        }
        return q;
    }
};
