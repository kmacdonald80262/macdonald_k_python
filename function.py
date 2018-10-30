def greetings():
        print("Hello from the greetings function")


# the greetings function just says hello
# invoke or call the function
greetings()

def greetingsWithArgs(msg):
    print("now we are saying", msg, "from another function")


greetingsWithArgs("hey! sup!") 
greetingsWithArgs("something different")

myNumberVariable = 10


# returning values from functions (very powerful)
def someMath(num1=2, num2=4):
    global myNumberVariable
    
    myNumberVariable - num1 + num2
    return num1 + num2


sum = someMath()
print("we are doing some math and getting", sum)


sum= someMath(10, 15)
print("another math operation with", sum, "as the result")


# variables and scope

