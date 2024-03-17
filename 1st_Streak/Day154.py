# Problem : Time Needed to Inform All Employees
# Problem Statement : A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
# The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.
# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
# Return the number of minutes needed to inform all the employees about the urgent news.
from collections import defaultdict
class Solution:
    def dfs(self, manager, informTime, adjList):
        maxTime = 0
        for subordinate in adjList[manager]:
            maxTime = max(maxTime, self.dfs(subordinate, informTime, adjList))
        return maxTime + informTime[manager]

    def numOfMinutes(self, n, headID, manager, informTime):
        adjList = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                adjList[manager[i]].append(i)
        
        return self.dfs(headID, informTime, adjList)