class RecentCounter:

    def __init__(self):
        self.counter = []
        self.cached_index = 0
        
    def ping(self, t: int) -> int:
        self.counter.append(t)

        for i in range(self.cached_index, len(self.counter)):
            if t - self.counter[i] > 3000:
                self.cached_index += 1
            else:
                break
        
        return len(self.counter) - self.cached_index 

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)