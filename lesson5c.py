# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)

def simpleinterest():
    principal = 45000
    rate = 7
    time = 8
    simpleinterest = principal * rate * time 
    print("The simpleinterest is:", simpleinterest)
simpleinterest()
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

def simpleinterest(principal, rate, time):
    product = principal* rate * time
    print(product)
simpleinterest(3600, 4,7)

