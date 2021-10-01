import sys
size = 10
def create_generator(size):
    print('START')
    for number in range(size):
        print('***')
        yield number**2

my_obj = create_generator(size)
print(type(my_obj))
print(next(my_obj))
for n in my_obj:
    print('>>',n)