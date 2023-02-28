// Problem : Find Duplicate Subtrees
// Problem Statement : Given the root of a binary tree, return all duplicate subtrees.
// For each kind of duplicate subtrees, you only need to return the root node of any one of them.
// Two trees are duplicate if they have the same structure with the same node values
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
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
    string serializeSubtrees(TreeNode *node, unordered_map<string, int> &subtrees, vector<TreeNode *> &duplicates)
    {
        if (!node)
            return "#";
        string left = serializeSubtrees(node->left, subtrees, duplicates);
        string right = serializeSubtrees(node->right, subtrees, duplicates);
        string s = left + "," + right + "," + to_string(node->val);
        if (subtrees[s] == 1)
            duplicates.push_back(node);

        subtrees[s]++;
        return s;
    }
    vector<TreeNode *> findDuplicateSubtrees(TreeNode *root)
    {
        unordered_map<string, int> subtrees;
        vector<TreeNode *> duplicates;

        serializeSubtrees(root, subtrees, duplicates);

        return duplicates;
    }
};
int main()
{

    return 0;
}