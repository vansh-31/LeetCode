// Problem : Maximum Depth of Binary TreeMaximum Depth of Binary Tree
// Problem Statement : Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution
{
    struct TreeNode
    {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {}
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };
public:
    void solve(TreeNode *root, int height, int &mx)
    {
        if (root == NULL)
        {
            mx = max(mx, height);
            return;
        }
        solve(root->left, height + 1, mx);
        solve(root->right, height + 1, mx);
    }
    int maxDepth(TreeNode *root)
    {
        int mx = 0;
        solve(root, 0, mx);
        return mx;
    }
};
int main()
{

    return 0;
}