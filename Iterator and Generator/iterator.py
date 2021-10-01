#Iterator
s ='123'
iter_list = iter(range(10,15))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

class MyNumber:
    def __iter__(self):
        self.value = 1
        return self
    def __next__(self):
        value = self.value
        if value < 1000:
            self.value += 1
            return value
        else:
            raise StopIteration

for i in MyNumber():
    print(i)

numbers = MyNumber()
iter_num =iter(numbers)
print(next(iter_num))
print(next(iter_num))


