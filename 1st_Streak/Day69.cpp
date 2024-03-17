// Problem : Linked List Random Node
// Problem Statement : Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

// Implement the Solution class:

// Solution(ListNode head) Initializes the object with the head of the singly-linked list head.

// int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
    vector<int> v;
    int n;

public:
    Solution(ListNode *head)
    {
        ListNode *ptr = head;
        while (ptr)
        {
            v.push_back(ptr->val);
            ptr = ptr->next;
        }
        n = v.size();
    }

    int getRandom()
    {
        static int i = 0;
        if (i == 0)
        {
            srand(time(NULL));
            i++;
        }
        return v[rand() % n];
    }
};
int main()
{
    
    return 0;
}