#PYTHON FUNCTIONS : They are a block of code/ statements that performs a given task / action. They can be re-used throughout the program to perform different tasks 
#Functions are defined using 
#We have two main types i.e 
#Inbuit functions. They come pre-installed with the interpretor i.e print, prop, range, append( e.t.c)
#User-defined functions They are created bty a programmer to solve a given task
#to define a function you need to give it a name followed by parenthesis
#For the function body it is usualy indented and to invoke a function we use the function name 

def greetings():
    print("Hello, how are you?")
#below is the function  
greetings()

print("================")
#Addition Function 
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is:", sum)
addition()

print("============")
#create a function that is able to multiply thre values 
def multiplacation():
    num3 = 20
    num4 = 30
    num5 = 15
    product = num3 * num4 * num5
    print("The product of the numbers is:", product)
multiplacation()

print("============")
#Below is a division function 
def divide():
    number1 = int(input("Enter the first number"))
    number2 = int(input("Enter the second number"))
    quotient = number1 / number2
    print("The number is: ", quotient)
    

for function in range(3):
    divide()