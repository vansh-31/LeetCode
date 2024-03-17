# Problem : Can Place Flowers
# Problem Statement : You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n==0:
            return True
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                return n<=1
            if flowerbed[0]==1:
                return n<=0
        if flowerbed[0]==0 and flowerbed[1]==0:
            n-=1
            flowerbed[0] = 1
            if n<=0:
                return True
        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2]==0:
            n-=1
            flowerbed[len(flowerbed)-1] = 1
            if n<=0:
                return True
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                flowerbed[i] = 1
                n-=1
            if n<=0:
                return True
        return False