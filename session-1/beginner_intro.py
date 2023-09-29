'''
INTRO TO PYTHON

Beginner Notes
'''



# this is a comment
# the program will ignore comments
# they are for developer use

# variables
name = "Ivan"
age = 19

print(name, "is", age, "years old.")

# suppose a year passes
age = 20
print(name, "is", age, "years old.")


# arithmatic

x = 5
y = 3

add = x + y
sub = x - y
mul = x * y
div = x / y
exp = x ** y

# modulus gets the remainder
mod = x % y


# increment x by y
# x = x + y
x += y

# decrement x by y
# x = x - y
x -= y

# This also works for other operators
x *= y
x /= y


# if statements

condition1 = True
condition2 = False

if condition1:
    print("Condition1 is True")
elif condition2:
    print("Condition1 is False, but Condition2 is True")
else:
    print("Both Condition1 and Condition2 are False")



x = 5
y = 9

x += 5

if x < y:
    print("x < y")
elif y > x:
    print("x > y")
else:
    print("x == y")



# thats my note for myself
# for p in itertools.permutations('ABCD'):


# loops! :)

i = 1
while i < 10:
    print(i)
    i += 1

for i in range(0,10):
    print(i)

sample_list = ['this', 'is', 'a', 'list', ':)']
for item in sample_list:
    print(item)


# recursion
def recursive_loop(number):
    if(number > 0):
        print(number)
        return recursive_loop(number - 1)
    else:
        print(number)
        return

recursive_loop(5)


# iterables

# iterables are a collection of items
# that can be iterated over
# usually in a loop

sample_list = ['i', 'am','stressed', 'for', 'my', 'cosc', 328, 'midterm']
print(sample_list)

print("You can access elements by index")
print("Remember python indexes from zero to follow industry standards")
print("Element 6:", sample_list[6])

print("You can also access elements in reverse with the '-' character")
print("Note this does not start from zero")
print("Element -2", sample_list[-2])

# changing the data in a list

sample_list[6] = 320
print("The new class is COSC", sample_list[6])

# adding to a lust

sample_list.append("and final")
print(sample_list)

# append vs extend

list_1 = ['cat', 'dog', 'log']
list_2 = ['frog', 'bog']

list_1.append(list_2)
print("Append:")
print(list_1)
print(list_1[3])


list_1 = ['cat', 'dog', 'log']
list_2 = ['frog', 'bog']

list_1.extend(list_2)
print("Extend:")
print(list_1)
print(list_1[3])

sample_tuple = ('cosc', 328, 'should', 'stay', 'an', 'immutable', 'unit')
print(sample_tuple)
print("Element 4:", sample_tuple[3])

try:
    # this will raise an exception
    sample_tuple[1] = 320
except Exception as e:
    print(e)



sample_set = {'a', 'duplicate', 'in', 'a', 'set', 'is', 'deleted'}
print(sample_set)

try:
    # this will raise an exception
    print(sample_set[1])
except Exception as e:
    print(e)

# dictionaries

my_dict = {1:'one', 2:'two', 3:'three', 4:'four'}
print(my_dict)
print("my_dict[1]:", my_dict[1])

my_dict["five"]=5
print(my_dict)
print(my_dict["five"])


# list comprehension
 
some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
negative_evens = [-i for i in some_list if i % 2 == 0]

# the equivalent code without list comprehension

negative_evens = []
for i in some_list:
    if i % 2 == 0:
        negative_evens.append(-i)


# Functions


def example_fucntion(parameter1, parameter2):
    ''' i am a comment explaining what the function does '''
    variable = parameter1 + 10
    
    output = 0
    if variable > parameter2:
        for i in range(0, parameter2):
            output += (variable - i)
    else:
        output = parameter2
    
    return output

def function_in_fuction():
    # you can have a function in a function
    print('a=4, b=9, c=-10, d=9')
    sum = add_all(4,9,-10,9)
    print('the sum of a, b, c, d is', sum)


def add_all(a, b, c, d=0):
    # if d is not given into the function,
    # the value of d is zero by default
    return a + b + c + d

print("Passed in:")
print(add_all(1,2,3,4))
# passed in: 10

print("\nNot Passed in:")
print(add_all(1,2,3))
# not passed in 6






# Object Oriented Programming


class Robot:
    '''
    This is a Robot
    '''
    # this is a constructor
    def __init__(self, metal_type, ai=True):
        # this is how you declare an attribute (self.attribute)
        self.metal_type = metal_type
        self.ai=ai
    
    def do_robot_thing(self):
        # i am a function
        # you have to use self to access object methods
        self.spin()
    
    def spin(self):
        print("wee!!")


class SpecialRobot(Robot):
    '''
    This is a Robot that has been extended to have a special item
    the (Robot) denotes that this class extends Robot
    '''
    def __init__(self, metal_type, ai=True, special_item='love and affection'):
        super(Robot)
        self.special_item = special_item
    
    def use_special_item(self):
        return self.special_item
    
    def change_special_item(self):
        new_item = input('What is the Robot\'s new item?')
        print("Changing Robot's item to", new_item)
        self.special_item = new_item


# instanciating 
robot_1 = Robot("aluminum")
robot_1.do_robot_thing()

robot_2 = SpecialRobot("tin", True, "bat")
robot_2.do_robot_thing()
robot_2.change_special_item()

