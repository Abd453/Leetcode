class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = []
        for i in range(rowIndex+1):
          temp = [1]*(i+1)
          for j in range(1,i):
            temp[j] = prev[j] + prev[j-1]
          prev = temp
        
        return temp
        