class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for i in operations:
            if i=="X++" or i== "++X":
                X=X+1
            elif i== "X--" or i== "--X":
                X=X-1
        return X

        #Increment and decrement the number
        
        #store the numbers iteratively things iteratively
        #then return the final result
        