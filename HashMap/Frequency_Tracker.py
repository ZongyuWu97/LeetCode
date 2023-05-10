class FrequencyTracker:

    def __init__(self):
        self.numbers = defaultdict(int)
        self.frequencies = defaultdict(set)
        

    def add(self, number: int) -> None:
        self.numbers[number] += 1
        frequency = self.numbers[number]
        self.frequencies[frequency].add(number)
        
        if frequency > 1:
            self.frequencies[frequency - 1].remove(number)

    def deleteOne(self, number: int) -> None:
        if self.numbers[number] == 0:
            return
        
        self.numbers[number] -= 1
        frequency = self.numbers[number]
        self.frequencies[frequency].add(number) 
        self.frequencies[frequency + 1].remove(number)
        

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.frequencies[frequency]) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)