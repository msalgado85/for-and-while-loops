#WHILE LOOPS EXAMPLES

#EXAMPLE 1

# while loop = execute some code WHILE some conditions remains true
name = input('enter your name: ')

while name == "":
    print('You did not enter your name')
    name = input('enter your name: ')
    #When you don't have a way to escapre yout while loop it becomes an infinite loop ctrl + c stops the command.
else:
    print(f"Hello {name}")
#itteration = loops

# EXAMPLE 2

age = int(input('enter your age: '))
while age <0:
    print('nuh uh youre not a negative age silly')
    age = int(input('enter your age'))
print(f'you are {age} years old, you unc')

#EXAMPLE 3

food = input('Enter a food you like: ')
while not food == 'q':
    print(f"you like {food}")
    food = input('Enter a food you like: ')
print('bye ')

#Example 4

num = int(input('enter a # between 1-10: '))
while num < 1 or num > 10:
    print(f'{num} is not valid silly')
    num = int(input('enter a # between 1-10: '))
print(f'Your number is {num}')

#FOR LOOPS EXAMPLES

#for loops = execute a block of code a fixed number of times.
#   You can literate over a range, string, sequence, etc.

#EXAMPLE 1

for x in reversed(range(1, 11)):
    print(x)
#x is just a wariable 

print("HAPPY NEW YEARS! ")
#reversed makes you count backwards,

credit_card = '1234-5678-9012-3456'

for x in credit_card:
    print(x)

#EXAMPLE 2

#CONTINUE SKIPS THE NUMBER GIVEN

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

#BREAK OR RETURN STOPS THE EXECUTION
        
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

#CHALLANGE

#1.
list_of_names = ['John', 'Paul', 'George', 'Ringo', 'Daniel']

for name in list_of_names:
    if name == 'George':
        print('George was found')
    else:
        print('George was not found')
        print(name)

#2.
list_of_names = ['Thanos', 'Ironman', 'Thor', 'Hulk']
for name in list_of_names:
    if name == 'Ironman':
        continue
    print(name)

#3.
list_of_names = ['Thanos', 'Ironman', 'Thor', 'Hulk']
for name in list_of_names:
    if name == 'Thanos':
        name = 'Black Widow'
    print(name)