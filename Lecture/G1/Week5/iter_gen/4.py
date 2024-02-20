class MyNums:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
        
    def __next__(self):
        x = self.start
        if x > self.stop:
            raise StopIteration
        self.start += 1
        return x
    
mynums = MyNums(1, 20)

mynums_iter = iter(mynums)

for num in mynums:
    print(num)