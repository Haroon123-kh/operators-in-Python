# operators-in-Python
Python Basics: Difference Between is and in Understanding the difference between is and in in Python is crucial for writing clean and correct code.  ✅ is Operator The is operator checks identity — whether two variables refer to the same object in memory.

python
Copy
Edit
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True – same object
print(a is c)  # False – same content, different objects
Use is when you want to compare object identity, like checking against None:

python
Copy
Edit
if a is None:
    pass
✅ in Operator
The in operator checks membership — whether an element exists within an iterable.

python
Copy
Edit
my_list = [1, 2, 3]
print(2 in my_list)  # True
print(5 in my_list)  # False
Use in to see if a value is contained in lists, tuples, sets, dictionaries, or strings.



