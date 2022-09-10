(a, b, c) = 1, 2, 3
print(a, b, c)

a, b, c = 3, 4, 5
print(a, b, c)

# unpacking string
a, b, c = '789'
print(a, b, c)

# unpacking list
a, b, c = [4, 7, 9]
print(a, b, c)

# unpacking generators
gen = (i ** 2 for i in range(3))
a, b, c = gen
print(a, b, c)

gen = (i * 2 for i in range(3))
a, b, c = gen
print(a, b, c)

gen = (i + 2 for i in range(3))
a, b, c = gen
print(a, b, c)

# unpacking dictionary
my_dict = {'one': 1, 'two': 2, 'three': 3}
a, b, c = my_dict  # unpacking keys
print(a, b, c)

a, b, c = my_dict.values()  # unpacking values
print(a, b, c)

a, b, c = my_dict.items()  # unpacking key value pairs
print(a, b, c)

a, b, c = range(3)
print(a, b, c)

a, b, c = range(3, 6)
print(a, b, c)

# unpacking sets
'''
Finally, we can also use set objects in unpacking operations. 
However, since sets are unordered collection, the order of the assignments can be sort of incoherent and 
can lead to subtle bugs.
If we use sets in unpacking operations, then the final order of the assignments can be quite different
from what we want and expect. So, it's best to avoid using sets in unpacking operations unless the 
order of assignment isn't important to our code.
'''
a, b, c = {"a", "b", "c"}
print(a, b, c)

# Packing With the * Operator
'''
The * operator is known, in this context, as the tuple (or iterable) unpacking operator. 
It extends the unpacking functionality to allow us to collect or pack multiple values in a single variable. 
In the following example, we pack a tuple of values into a single variable by using the * operator:
'''
*a, = 1, 2
print(a)

*a, = [1, 2, 3]
print(a)

'''
For this code to work, the left side of the assignment must be a tuple (or a list). 
That's why we use a trailing comma. This tuple can contain as many variables as we need. However, 
it can only contain one starred expression.
'''

a, *b, = 1, 2, 3, 4
print(a, b)

a, *b, = 1,
print(a, b)

*a, b, = 1, 2, 3
print(a, b)

*a, b, = 1,
print(a, b)

# Packing one value in a because b and c are mandatory:
*a, b, c = 1, 2, 3
print(a, b, c)

'''
Packing values in a variable with the * operator can be handy when we need to collect the 
elements of a generator in a single variable without using the list() function. 
In the following examples, we use the * operator to pack the elements of a generator expression 
and a range object to a individual variable:
'''
gen = (i ** 2 for i in range(10))
*a, = gen
print(a)

*r, = range(10)
print(r)

# Using Packing and Unpacking in Practice
