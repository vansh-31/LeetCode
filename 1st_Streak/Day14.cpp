// Problem : Binary Tree Preorder Traversal
// Problem Statement : Given the root of a binary tree, return the preorder traversal of its nodes' values.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;

//  * Definition for a binary tree node.
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
    void preOrder(TreeNode *root, vector<int> &pre)
    {
        if (root == NULL)
        {
            return;
        }
        pre.push_back(root->val);
        preOrder(root->left, pre);
        preOrder(root->right, pre);
    }
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> pre;
        preOrder(root, pre);
        return pre;
    }
};
int main()
{

    return 0;
}