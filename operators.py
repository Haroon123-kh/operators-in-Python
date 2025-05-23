
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True – same object
print(a is c)  # False – same content, different objects
if a is None:
    pass

my_list = [1, 2, 3]
print(2 in my_list)  # True
print(5 in my_list)  # False
