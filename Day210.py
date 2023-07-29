# Problem : Soup Servings
# Problem Statement : There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:
# Serve 100 ml of soup A and 0 ml of soup B,
# Serve 75 ml of soup A and 25 ml of soup B,
# Serve 50 ml of soup A and 50 ml of soup B, and
# Serve 25 ml of soup A and 75 ml of soup B.
# When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.
# Note that we do not have an operation where all 100 ml's of soup B are used first.
# Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1
        dp =  [ [-1 for _ in range(n+1) ] for _ in range(n+1)]
        def operation(a,b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            if dp[a][b] != -1:
                return dp[a][b]
            ans = 0
            ans += operation(a-100,b)
            ans += operation(a-75,b-25)
            ans += operation(a-50,b-50)
            ans += operation(a-25,b-75)
            dp[a][b] = (ans*0.25)
            return dp[a][b]
        return operation(n,n)