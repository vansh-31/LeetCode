// Problem : Invert Binary Tree
// Problem : Given the root of a binary tree, invert the tree, and return its root.
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
    void solve(TreeNode* root)
    {
        if (root==NULL)
        {
            return;
        }
        if (root->left != NULL && root->right != NULL)
        {
            swap(root->left,root->right);
            solve(root->left);
            solve(root->right);
        }
        else if (root->left)
        {
            root->right = root->left;
            root->left = NULL;
            solve(root->right);
        }
        else if (root->right)
        {
            root->left = root->right;
            root->right = NULL;
            solve(root->left);
        }
    }
    TreeNode *invertTree(TreeNode *root)
    {
        solve(root);
        return root;
    }
};
int main()
{

    return 0;
}