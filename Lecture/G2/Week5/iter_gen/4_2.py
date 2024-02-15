# Iterators and Generators

class MyNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.b:
            raise StopIteration
        x = self.a
        self.a += 1     
        return x   

mynums = MyNumbers(1, 10)

# not infinite now
for i in mynums:
    print(i)