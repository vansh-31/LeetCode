// Problem : Merge k Sorted Lists
// Problem Statement : You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.
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
class compare
{
public:
    bool operator()(ListNode *a, ListNode *b)
    {
        return a->val > b->val;
    }
};
class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        priority_queue<ListNode *, vector<ListNode *>, compare> minHeap;
        ListNode *head = new ListNode(-1);
        ListNode *tail = head;
        for (int i = 0; i < lists.size(); i++)
        {
            if (lists[i])
                minHeap.push(lists[i]);
        }
        while (!minHeap.empty())
        {
            ListNode *front = minHeap.top();
            cout << front->val << " ";
            minHeap.pop();
            tail->next = front;
            tail = front;
            if (front->next != NULL)
            {
                minHeap.push(front->next);
            }
        }
        return head->next;
    }
};
int main()
{

    return 0;
}