# Problem : Search a 2D Matrix
# Problem Statement : You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
from typing import List 
class Solution:
    def searchMatrix(self, arr: List[List[int]], key: int) -> bool:
        n,m = len(arr),len(arr[0])
        """First Method"""
        # low,high = 0,(n*m) - 1
        # while low<=high:
        #     mid = (low+high)//2
        #     row = mid//m
        #     col = mid%m
        #     if arr[row][col]==key:
        #         return True
        #     elif arr[row][col] < key:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return False
        """Second Method"""
        row = -1
        start,end = 0,n-1
        while start<= end:
            mid = (start+end)//2
            if arr[mid][0] <= key and arr[mid][-1] >= key:
                row = mid
                break
            if arr[mid][0] < key:
                start = mid+1
            else:
                end = mid-1
        if row == -1:
            return False
        col = -1
        start,end = 0,m-1
        while start <= end:
            mid = (start+end)//2
            if arr[row][mid] == key:
                col = mid
                break
            if arr[row][mid] < key:
                start = mid+1
            else:
                end = mid-1
        if col == -1:
            return False
        return True