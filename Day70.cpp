// Problem : Convert Sorted List to Binary Search Tree
// Problem Statement : Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
// height-balanced
//  binary search tree.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution
{
public:
    TreeNode *solve(vector<int> &list, int i, int j)
    {
        if (i > j)
        {
            return NULL;
        }
        int mid = (i + j) / 2;
        TreeNode *root = new TreeNode(list[mid]);
        root->left = solve(list, i, mid - 1);
        root->right = solve(list, mid + 1, j);
        return root;
    }
    TreeNode *sortedListToBST(ListNode *head)
    {
        vector<int> list;
        ListNode *ptr = head;
        while (ptr != NULL)
        {
            list.push_back(ptr->val);
            ptr = ptr->next;
        }
        return solve(list, 0, list.size() - 1);
    }
};
int main()
{

    return 0;
}