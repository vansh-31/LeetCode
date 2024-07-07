# Problem : Water Bottles
# Problem Statement : There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = empty = numBottles
        while empty >= numExchange:
            exchange = empty // numExchange
            drink += exchange
            empty = empty % numExchange
            empty += exchange
        return drink
