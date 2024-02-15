# Iterators and Generators

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1     
        return x   

mynums = MyNumbers()
nums_iter = iter(mynums)

print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))