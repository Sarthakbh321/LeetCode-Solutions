class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if(m*n != len(original)): return []
        
        result = [[None for _ in range(n)] for __ in range(m)]
        
        # Time -> O(len(original))
        for i in range(len(original)):
            row = i//n
            column = i%n
            result[row][column] = original[i]
        
        return result