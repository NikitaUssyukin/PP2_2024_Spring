class MyNums:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
mynums = MyNums()

# infinite loop
for num in mynums:
    print(num)