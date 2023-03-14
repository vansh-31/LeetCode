// Problem : Symmetric Tree
// Problem Statement : Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    bool check(TreeNode* left,TreeNode* right)
    {
        if(left == NULL && right == NULL)
        {
            return true;
        }
        if( left && right && left->val == right->val )
        {
            return check(left->left,right->right) && check(left->right,right->left);
        }
        return false;
    }
    bool isSymmetric(TreeNode* root)
    {
        return ( !root ? true : check(root->left,root->right) );
    }
};
int main()
{
    
    return 0;
}