class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = [None]*(len(prices))
        for i in range(len(prices)):
            if(len(stack) == 0):
                stack.append((prices[i], i))
            else:
                
                while(stack and prices[i] <= stack[-1][0]):
                    res[stack[-1][1]] = stack[-1][0]-prices[i]
                    stack.pop()
                
                stack.append((prices[i], i))
        
        for i in stack:
            res[i[1]] = i[0]
            
        return res
                    