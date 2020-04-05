# IF else and Booleans

Color = 'RED'

if Color == 'RED':
    print("Its Red!")

    # Other comparisons
    # Equal '==' , Not Equal '!=' , Greater/less as usual , Object Identity 'is'
    # Difference in == and 'is': is checks for the same object in the memory.
elif Color == 'BLUE':
    print("Its Blue!")
else:
    print('No match')

# Python has NO SWITCH case

# boolean operators: and , or , not (instead of && || operators)
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page!')
else:
    print('Bad credentials!')




