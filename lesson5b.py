#FUNCTIONS WITH PARAMETERS :
#They are values that get passsed as arguments given to a function inside of the parethesis.

def greetings(name):
    print(f"{name} How are you? Hope everything is fine. ")
greetings("Vallary")
greetings("Ashley")
greetings("Emmanuel")

print("======================")
def message (names):
    print(f"{names} Hello. We shall be having a generall meeting on date  ..... Please avail yourself ")
message("Joy")
message("Billy")

print("==================")
#Create a function that accepts parameters to add two numbers
def addition(x , y):
    sum = x + y
    print("The sum of the numbers is:", sum)
addition(23, 45)