# Problem : Decoded String at Index
# Problem Statement : You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
# Given an integer k, return the kth letter (1-indexed) in the decoded string.
class Solution:
    def decodeAtIndex(self, S, K):   
        A = [1]
        for x in S[1:]:
            if A[-1] >= K : break
            if x.isdigit():
                A.append( A[-1]*int(x) )
            else:
                A.append( A[-1]+1 )
        for i in range(len(A)-1,-1,-1):
            K %= A[i]
            if not K and S[i].isalpha():
                return S[i]