# Problem : Maximum Number of Achievable Transfer Requests
# Problem Statement : We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.
# You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer from building fromi to building toi.
# All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.
# Return the maximum number of achievable requests.
class Solution:
    def __init__(self):
        self.ans = 0

    def helper(self, start, requests, indegree, n, count):
        if start == len(requests):
            for i in range(n):
                if indegree[i] != 0:
                    return
            self.ans = max(self.ans, count)
            return

        # Take 
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start + 1, requests, indegree, n, count + 1)

        # Not-take
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1
        self.helper(start + 1, requests, indegree, n, count)

    def maximumRequests(self, n, requests):
        indegree = [0] * n
        self.helper(0, requests, indegree, n, 0)
        return self.ans