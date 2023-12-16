struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (left == right)return head;
        ListNode* p,*q = nullptr;
        ListNode* curr = head;
        for(auto i = 1; i<= right;i++){
            if(i == left-1)
            
        }
        // for(auto i = 1; i <= right; i++) {
            // if(left == right)return head;
            // curr = curr->next;
            // if(i >= left-1 && i<= right-1){
                // q = curr;
                // p = curr->next;
                // 
            // }
            // 
        // }
    // 
    }
};