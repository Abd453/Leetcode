class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for row in image:
            inverted_row = [1 - pixel for pixel in row[::-1]]
            result.append(inverted_row)
        return result
