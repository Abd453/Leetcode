# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         people = list(zip(names, heights))
#         for i in range(len(people)-1):
#             for j in range(len(people)-1-i):
#                     if people[j][1] <= people[j+1][1]:
#                        people[j],people[j+1] = people[j+1], people[j]
#                     names = [person[0] for person in people]
#         return names

    # 1. first i have to write acode so that i can sort the heights
    # 2. I have to make aconnection between the names and the height of the person 
    # 3. and the output of the sorted heights must give the repective individual names 

#using selection sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        for i in range(len(people)):
            min_index = i
            for j in range(i+1,len(people)):
                    if people[j][1] > people[min_index][1]:
                        min_index = j
            people[i],people[min_index] = people[min_index], people[i]
        names = [person[0] for person in people]
        return names

