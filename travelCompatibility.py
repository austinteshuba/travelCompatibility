# travelcompatibility.py
# Assumption: If there are two matches with the same similarities, return the first one.
# Assumption: Input will be a list in the proper format
def travelCompatibility(myTrendsArray, friendsTrendsArray):
    if myTrendsArray == None or len(myTrendsArray) == 0 or friendsTrendsArray == None or len(friendsTrendsArray)==0:
        return -1
    myTrends = set(myTrendsArray) #O(1)

    index = -1
    similarities = 0
    for i in range(len(friendsTrendsArray)):
        friendsTrends = set(friendsTrendsArray[i])
        iterSimilarities = len(myTrends & friendsTrends) # Get the intersection of the sets
        if iterSimilarities > similarities:
            index = i
            similarities = iterSimilarities
            if similarities == len(myTrends):
                return index

    return index

print(travelCompatibility(["A"], [["YXU"], ["BOS"], ["LGA"]]))

#Overall, assuming the amount of travel elements is much less than the amount of list entries, this is an O(n) algorithm.
#If the number of travel elements and amount of list entries are both sufficiently large, this is O(n^2)
    

    
