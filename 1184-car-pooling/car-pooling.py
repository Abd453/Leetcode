# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         dic = defaultdict(int)
#         for count, start, end in trips:
#             dic[start] += count
#             dic[end] -= count
        
#         presum = 0
#         for t in sorted(dic):
#             presum += dic[t]
#             if presum > capacity:
#                 return False
#         return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Create a list to store events
        events = []
        
        # Record pickup and drop-off events
        for count, start, end in trips:
            events.append((start, count))   # Add passengers at pickup
            events.append((end, -count))   # Remove passengers at drop-off
        
        # Sort events by time, resolving ties by passenger change
        events.sort()
        
        # Track the number of passengers in the car
        current_passengers = 0
        for time, passenger_change in events:
            current_passengers += passenger_change
            if current_passengers > capacity:
                return False
        
        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for count, start, end in trips:
            events.append((start, count))   
            events.append((end, -count))   
        events.sort()
        current_passengers = 0
        for time, passenger_change in events:
            current_passengers += passenger_change
            if current_passengers > capacity:
                return False
    
        return True
