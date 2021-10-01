import sys
#List
size = 100
my_list = [number ** 2 for number in range(size)]
print(my_list)
print(sys.getsizeof(my_list))
#for i in my_list:
#    print(i)

#Generator
my_generator = (number ** 2 for number in range(size))
print(my_generator)
print(sys.getsizeof(my_generator))
#for i in my_generator:
#    print(i)

