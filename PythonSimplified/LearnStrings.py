# All about dealing with Strings in Python

# direct print of string
print('hello world')

# to display two lines txt
text_to_display = """line1
line2"""
# print variable
print(text_to_display)

# to find length
print(len(text_to_display))  # next line is a character

# Access index
print(text_to_display[3])

# Access a word in string with index range: "SLICING"
print(text_to_display[0:5])  # first digit includes the character but upper limit doesn't
print(text_to_display[6:])  # leaving blank depicts last index (similar for beginning)

# Methods

# lower and upper case
print(text_to_display.upper())

# Count the occurrence
print(text_to_display.count('li'))  # displays how many time 'li' is there in that string

# Find where is the required word/letter in the string
print(text_to_display.find('line2'))  # Shows the index where 'line2' begins, if absent then returns -1

# Replacing something in the string
new_text = text_to_display.replace('line2', 'newline')  # Cannot print directly with replace as it replaces when we declare new variable.
print(text_to_display)  # still the original
print(new_text)  # new variable with replaced word
# can use same variable like this: " text_to_display = text_to_display.replace('line2', 'newline') "

# Adding or concatenating strings
word1 = 'Hello'
word2 = 'Universe'
new_word = word1 + ' ' + word2 + "!"
print(new_word)  # Another recent method of doing this is version above 3.6 is using F string: f'{} {} with placeholders

# trick for finding all the attributes and method linked to any variable (like help)
print(dir(new_word))  # specific to variable
print(help(str))  # specific for strings and for specific selection for implementation: "help(str.lower())"