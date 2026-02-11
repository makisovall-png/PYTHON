# create a python progrsm thst will determine whether the number entered is an even number or an odd number 
#number = int(input("Enter your number"))
#if number % 2 ==0:
  #  print("the number is even")
#else:
   # print("the number is odd")

#create a python progam that will be able to determine if a person can donate blood based on the weight and age of the person. if the weight is above 50kgs and the age is above 18 the person can donate blood, else not possible

age = int(input("enter the age"))
weight = int(input("enter the weight"))

if weight >=50 and age >=18 :
    print("can donate")
else:
    print("impossible")