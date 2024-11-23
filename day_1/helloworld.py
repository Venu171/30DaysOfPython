# Import system library
import sys
# Import math Library
import math
# -------- Exercise-1: Day-1(Level-1)--------#

# 1.Check the python version you are using
# Ans: Using `python --version--` in the terminal gives the version of python
print(sys.version)

"""
2.Open the python interactive shell and do the following operations. 
The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)
"""
"""
>>> 3+4(addition)
7
>>> 3-4(subtraction)
-1
>>> 3*4(multiplication)
12
>>> 3%4(Modulo operator--returns remainder)
3
>>> 3/4(Integer division--returns only integer number with decimals)
0.75
>>> 3**4(Exponentiation(power))
81
>>> 3//4(Floor Division(returns only integer number))
0
>>>
"""

"""
3.Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python
"""

# Answer
"""
>>> my_name="Venu"
>>> my_family_name="Pelluru"
>>> my_country="India"
>>> my_string="I am enjoying 30 days of python"
"""

my_name = "Venu"
my_family_name = "Pelluru"
my_country = "India"
my_string = "I am enjoying 30 days of python"

"""
4.Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country
"""
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(my_name))
print(type(my_family_name))
print(type(my_country))


# -------- Exercise-1: Day-1(Level-2)--------#

"""
1.Create a folder named day_1 inside 30DaysOfPython folder.
Inside day_1 folder, create a python file helloworld.py 
and repeat questions 1, 2, 3 and 4.
Remember to use print() when you are working on a python file.
Navigate to the directory where you have saved your file, and run it.
"""
# Ans: Already written🥳


# -------- Exercise-1: Day-1(Level-3)--------#

"""
1.Write an example for different Python
data types such as Number(Integer, Float, Complex),
String, Boolean, List, Tuple, Set and Dictionary.
"""

# Ans:Example for different data types

# Number(Integer, Float, Complex)
my_int = 2
my_float = 3.54
my_complex = 3-4j
my_string2 = "I love Python"
my_boolean1 = True
my_boolean2 = False
my_list = ["Hello", "World", 1, 2, 4]
my_tuple = ("Hello", "World", 1, 2, 4)
my_set = {1, 2, 4, "Hello", "World"}
my_dictionary = {
    "name": "Venu",
    "profession": "Software Developer"
}

"""
2.Find an Euclidian distance between (2, 3) and (10, 8)
"""

# Ans:
# In one dimension formula is |p-q|


def distance_between_two_co_ordinates(p, q):
    p1, p2 = p
    q1, q2 = q
    distance = math.sqrt((p1-q1)**2+(p2-q2)**2)
    return distance


print(distance_between_two_co_ordinates((2, 3), (10, 8)))
