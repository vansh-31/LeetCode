# Problem : Average Waiting Time
# Problem Statement : There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:
# arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
# timei is the time needed to prepare the order of the ith customer.
# When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.
# Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current_time = 0
        total_waiting_time = 0

        for arrival, time_needed in customers:
            if current_time < arrival:
                current_time = arrival
            finish_time = current_time + time_needed
            waiting_time = finish_time - arrival
            total_waiting_time += waiting_time
            current_time = finish_time

        average_waiting_time = total_waiting_time / len(customers)
        return average_waiting_time
