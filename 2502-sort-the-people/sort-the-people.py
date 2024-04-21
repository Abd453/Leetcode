class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict({i: heights[i] for i in range(len(names))})
        sorted_indexes = sorted(d, key=lambda x: d[x], reverse=True)
        sorted_names = [names[i] for i in sorted_indexes]
            
        return sorted_names