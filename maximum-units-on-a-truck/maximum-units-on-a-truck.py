class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        
        res = 0
        print(boxTypes)
        for i in boxTypes:
            chosen = min(truckSize, i[0])
            res += chosen*i[1]
            truckSize -= chosen
        
        return res