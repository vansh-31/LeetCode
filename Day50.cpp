// Problem : Binary Tree Zigzag Level Order Traversal
// Problem Statement : Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
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
    vector<vector<int>> zigzagLevelOrder(TreeNode *root)
    {
        vector<vector<int>> ans;
        if (root==nullptr)
        {
            return ans;
        }
        stack<TreeNode *> even;
        stack<TreeNode *> odd;
        even.push(root);
        int lvl = 0;
        while (!even.empty() || !odd.empty())
        {
            vector<int> temp;
            TreeNode *top;
            if (lvl % 2 == 0)
            {
                while (!even.empty())
                {
                    top = even.top();
                    even.pop();
                    temp.push_back(top->val);
                    if (top->left)
                    {
                        odd.push(top->left);
                    }
                    if (top->right)
                    {
                        odd.push(top->right);
                    }
                }
            }
            else
            {
                while (!odd.empty())
                {
                    top = odd.top();
                    odd.pop();
                    temp.push_back(top->val);
                    if (top->right)
                    {
                        even.push(top->right);
                    }
                    if (top->left)
                    {
                        even.push(top->left);
                    }
                }
            }
            ans.push_back(temp);
            lvl++;
        }
        return ans;
    }
};
int main()
{

    return 0;
}