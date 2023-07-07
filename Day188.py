# Problem : Maximize the Confusion of an Exam
# Problem Statement : A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).
# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:
# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maximize(target):
            left = right = diff = res = 0
            while right < len(answerKey):
                #if character at index right is not target we increment diff since we are including it in our subArray
                if answerKey[right] != target:
                    diff += 1
                #until diff > k we have to move left index towards right
                while diff > k:
                    #if character atindex left is not target, we decrement diff (since we are moving left and exlcuding this from our current subArray)
                    if answerKey[left] != target:
                        diff -= 1
                    #increment left
                    left += 1
                #update result
                res = max(res, right-left+1)
                right += 1
            return res
        return max(maximize("T"), maximize("F"))
        