
import test_module as tm
# or directly import the function(if need the function only) : "from test_module import find_index"

courses = ['History','Science','English','Math']

index = tm.find_index(courses,'Math')
print(index)

# Importing standard libraries
import random    # std lib to get random value
random_course = random.choice(courses)
print(random_course)