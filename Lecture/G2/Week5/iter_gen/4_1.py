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

# infinite loop
for i in mynums:
    print(i)