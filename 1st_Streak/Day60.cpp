// Problem : Sort an Array
// Problem Statement : Given an array of integers nums, sort the array in ascending order and return it.
// You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define MOD 1000000007
#define PI 3.14
using namespace std;
class Solution {
public:
    void Merge(vector<int> &A, int s, int e, int mid)
{
    int l_size = mid-s+1;
    int r_size = e - mid;

    int* left = new int[l_size];
    int* right = new int[r_size];
    int k = s;
    for (int i = 0; i < l_size; i++)
    {
        left[i] = A[k++];
    }
    k = mid+1;
    for (int i = 0; i < r_size; i++)
    {
        right[i] = A[k++];
    }
    int i = 0,j = 0;
    k = s;
    while (i<l_size && j < r_size)
    {
        if (left[i]<right[j])
        {
            A[k++] = left[i++];
        }
        else
        {
            A[k++] = right[j++];
        }
    }
    while (i<l_size)
    {
        A[k++] = left[i++];
    }
    
    while (j<r_size)
    {
        A[k++] = right[j++];
    }
    delete[] left;
    delete[] right;
}
void MergeSort(vector<int> &A, int s, int e)
{
    if (s >= e)
    {
        return;
    }
    int mid = (s + e) / 2;
    MergeSort(A, s, mid);
    MergeSort(A, mid + 1, e);
    Merge(A, s, e, mid);
}
    vector<int> sortArray(vector<int>& nums)
    {
        MergeSort(nums,0,nums.size()-1);
        return nums;
    }
};
int main()
{

    return 0;
}