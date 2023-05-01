# Problem : Average Salary Excluding the Minimum and Maximum Salary
# Problem Statement : You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
class Solution:
    def average(self, salary: list[int]) -> float:
        return float(sum(sorted(salary)[1:-1]))/float(len(salary)-2)