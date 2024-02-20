class MyNums:
    def __iter__(self):
        self.start = 1
        return self
        
    def __next__(self):
        x = self.start
        self.start += 1
        return x
    
mynums = MyNums()

mynums_iter = iter(mynums)

print(next(mynums_iter))
print(next(mynums_iter))
print(next(mynums_iter))
print(next(mynums_iter))
print(next(mynums_iter))