// Problem : Add Two Numbers
// Problem Statement : You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
//  * Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *head = new ListNode(-1);
        ListNode *tail = head;
        int carry = 0;
        while (l1 != nullptr || l2 != nullptr || carry != 0)
        {
            int val1 = 0;
            int val2 = 0;
            if (l1 != nullptr)
            {
                val1 = l1->val;
            }
            if (l2 != nullptr)
            {
                val2 = l2->val;
            }
            int sum = val1 + val2 + carry;
            carry = sum / 10;
            ListNode *temp = new ListNode((sum % 10));
            tail->next = temp;
            tail = temp;

            if (l1 != nullptr)
                l1 = l1->next;

            if (l2 != nullptr)
                l2 = l2->next;
        }
        return head->next;
    }
};
int main()
{

    return 0;
}