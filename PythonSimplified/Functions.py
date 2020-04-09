# Create function by defining it with "def"

def hello_world():
    pass    # This simply means that we'll not be doing anything here for now and also not get errors for the same

# Later we can call this function anytime:
hello_world()  # Calling the function
print(hello_world)      # Without "()"
print(hello_world())    # With "()" says "None" as there is no return

# Now let's play with it:

def print_fun():
    print('Hello World!')

print_fun()

# Function with a "return" when you want to return something on calling a function

def return_string():
    return "I am returned!"

return_string()     # Now this will not print because now the function is assigned a return value
print(return_string())  # this shows that value of this function called is the returned item

# NOTE: Since this return type is string, so we can do any string operation(previous lessor) with this function :)

# Passing "Parameters" in functions:
def test_func(param):
    return '{} Sam!'.format(param)

print(test_func('Bonjour'))

# *args and **kwargs argument and key word argument in function parameter
def information(*args, **kwargs):
    print(args)  # its a tuple
    print(kwargs)   # its a dictionary

information('Red', 'Blue','Orange',dress_type='shirt', gender='Male')

# an example for understanding the most

month_days = [0,31,28,31,30,31,30,31,30,31,30,31]

def is_leap(year):
    """ Return true for leap years """
    return year % 4 == 0 and (year % 100 != 0 or year% 400 == 0)

def days_in_month(year, month):
    """ Return number of days in that month in that year"""

    if not 1 <= month <= 12:
        return 'invalid month'

    if month == 2 and is_leap(year):
        return  29

    return month_days[month]