// Problem : Minimum Distance Between BST Nodes
// Problem Statement : Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
public:
    struct TreeNode
    {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };
    TreeNode *previous = nullptr;
    int min = INT_MAX;
    int minDiffInBST(TreeNode *root)
    {
        inOrder(root);
        return min;
    }
    void inOrder(TreeNode *root)
    {
        if (root == nullptr)
            return;
        inOrder(root->left);
        if (previous != nullptr)
        {
            min = std::min(min, root->val - previous->val);
        }
        previous = root;
        inOrder(root->right);
    }
};
int main()
{

    return 0;
}