# functions
# def<function name>(parameter):
# logic
# use of fucntion

# example
# def greet():
#     print('hello, welcome to backend lavender')

# # call greet()
# greet()

# positional argument
def introduce(name):
    print(f'Hi, i am {name}. Welcome to today\'s class. ')
    name = name

introduce('johnathan')
introduce('marianne')

# introduce return
def introduce(name):
    print(f'Hi, i am {name}. Welcome to today\'s class. ')
    
    return name + "" +"Joey"
print(introduce('Iris'))

def square(num):
    return num * num  

print (square(5))

def multiply(num):
    return num ** 2


def add(num):
    result = multiply(num)
    return num + result

print(add(4))

def Area(length, width):
    return length * width

def volume(length, width, height):
    return length * width * height

answer = Area(5,7)
res = volume(4,8,9)

print(answer,res )
