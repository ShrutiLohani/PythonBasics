# Dictionary: Same as key-value pairs, Hash map etc.
student = {'name':'John','age':'24','course':['PCM','SCI']}
print(student['course'])

# Other way to get the key
print(student.get('blabla'))   # It will say "None" as this key is absent (instead of giving error)
student.update({'name':'Jane','age':'23'})   # It will update the student set
print(student)
del student['age']  # delete the pair with the specified key
# Also can use "pop" and save to different variable
course = student.pop('course')
print(course)
# to check how many keys
print(len(student))
# name all the keys
print(student.keys())  # similar to values or 'items'

# FOR loop
for key,value in student.items():
    print(key,value)            # Prints all the key and value in student. Item simily means the number of pairs in dictionary



