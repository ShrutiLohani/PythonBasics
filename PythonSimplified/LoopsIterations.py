#  FOR & WHILE LOOP

# e.g. List of numbers

numbers = [1, 2, 3, 4, 5, 6, 7]

# For loop simply will pass through each entity (say "nums" (or "i"))
for nums in numbers:
    print(nums)  # This will print out each entity "nums" from list of numbers

# Now let's check what else we can do with this: "break" & "continue"
for i in numbers:
    print(i)
    if i==3:
        break
    else:
        print('Lesser than 3, I am', i)      # We can see that after i=3 this statement was not printed because of "Break" in the loop!

# However with continue its like:
for j in numbers:
    if j == 4:
        print('I am number 4!')
        continue
    print(j)           # We can see here that when condition was true it printed and then "continued" to loop

# Now,Let's check loop within loop
for value in numbers:
    for letters in "HOWEVER":
        print(letters)      # This will print each letter times the value in numbers (SO SIMPLE!)
        print(letters, value)  # to compare easily

# Concept of RANGE in loops when we need specific "range of loops"
for n in range(1,11):
    print(n)        # It will print out the range from 1-10

# Moving to WHILE loop
digit = 0

while digit < 10:
    print('single Digit number', digit)     # Print only if condition is true i.e. less than 10
    digit += 1      # Incrementing by 1 with every iteration

