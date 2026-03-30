class RecentCounter:

    def __init__(self):
        self.time = []

    def ping(self, t: int) -> int:
        self.time.append(t)

        while self.time and self.time[0] < t-3000:
            self.time.pop(0)
        return len(self.time)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)