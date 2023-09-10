# Problem : 
# Problem Statement : Given n orders, each order consist in pickup and delivery services. 
# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
# Since the answer may be too large, return it modulo 10^9 + 7.
class Solution:
    def countOrders(self, n: int) -> int:
        def fact(n):
            x = 1
            for i in range(2,n+1):
                x *= i
            return x
        return (fact( n<<1 ) // (1<<n) ) % (10**9+7)