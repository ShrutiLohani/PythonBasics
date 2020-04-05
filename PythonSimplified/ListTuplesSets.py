# List and Tuples allow to work with Sequential data
# Sets: Unordered collection of values with no duplicates

# Lists : Its like "array"
# e.g. List of courses
courses = ['Physics', 'Maths', 'Chemistry', 'Biology']

# length of list
print(len(courses))
# access the specific positioned course
print(courses[0])
# To access the last index in the List, we can use " -1 "
print(courses[-1])
# Similar to strings case for accessing the range
print(courses[0:3])  # Includes 0 position but less than 3 and [0:] : means till the end

# Add new course in the List
courses.append('CompSci')  # This adds the course in the end index of the list
# to add any course at specific index
courses.insert(2, 'English')

# Merging two Lists: say we have another list of courses2
courses2 = ['Art', 'Economics']
courses.append(courses2)

# REMOVING
courses.remove('Biology')  # Removes specific
courses.pop()  # Removes the last value from list

# REVERSING the order in list
courses.reverse()

# SORTING
courses.sort()
courses.sort(reverse=True)  # Reverse to Decreasing order

# To get min , max , sum(for list of numbers) simply use the functions (based on sorting)
print(max(courses))

# To get the index of particular value in the list
courses.index('Physics')

# For loop in list
for item in courses:
    print(item)  # This will print all the items in the list in new line
# BUT if we want index as well then:
for index, item in enumerate(courses):  # enumerate to add the index as well
    print(index, item)
# AND if we want to start at specific index for the loop then
for index, item in enumerate(courses, start=1):  # loop starts at index 1 of the list
    print(index, item)

# Modifying the list values
courses_string = ' , '.join(courses)  # Converting list into One string separated with anything: space, comma, nothing
print(courses_string)

# To do the reverse : String into List
new_list = courses_string.split(' , ')  # Remove the specified separator and convert to list
print(new_list)

#      TUPLES : These're non-mutable (cannot be changed unlike list)
# tuple are denoted with () : these brackets
tuple_1 = ('red', 'blue', 'green')
tuple_2 = tuple_1
# tuple_1[1] = 'orange'  # This gives error as tuple doesn't support item assignment
# SO no operations of adding/removing etc like list


#       SETS : denoted as list but with paranthesis {} unlike tuples() and list[]
seasons = {'winter', 'summer', 'spring'}
print(seasons)  # print is of different order and it removes duplicates

# To get intersection in two sets
seasons2 = {'fall', 'summer', 'rainy'}
print(seasons.intersection(seasons2))
# To get the difference in sets
print(seasons.difference(seasons2))
# To get the union
print(seasons.union(seasons2))

# How to create empty list, tuples, sets
empty_list = []
emptyList = list()     # both works for list
empty_tuples = ()
emptyTuples = tuple()  # both works for tuples
empty_sets = {} # This DOESN'T WORK it actually makes a DICTIONARY
emptySets = set()      # Only th function works for sets


