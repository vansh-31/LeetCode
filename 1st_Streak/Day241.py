# Problem : Minimum Penalty for a Shop
# Problem Statement : You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
# if the ith character is 'Y', it means that customers come at the ith hour
# whereas 'N' indicates that no customers come at the ith hour.
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
# For every hour when the shop is open and no customers come, the penalty increases by 1.
# For every hour when the shop is closed and customers come, the penalty increases by 1.
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.
# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_count = count = bestCloseTime = 0
        for i in range(len(customers)):
            count += 1 if customers[i] == "Y" else -1
            if count > max_count:
                max_count = count
                bestCloseTime = i+1
        return bestCloseTime