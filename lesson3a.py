#Boolean: this is adata type that evaluates to either true or false

isRaining = False 
print(isRaining)
print(type(isRaining))

paidloan = True 
print(paidloan)
print(type(paidloan))

#comparison operators: They are used to compare two or more statements and they usually return a bolean answer

number1 = 2
number2 = 5
print("Is number one greater than number two?", number1 > number2)
print("Is number one less than number two?", number1 < number2)
print("Is number one greater than or equal to number two?", number1 >= number2)
print("Is number one less than or equal to number two?", number1 <= number2)
print("Is number one equal to number two?", number1 == number2)
print("Is number one not equal to number two?", number1 != number2)

#Logical Operators:
#Logocal and : It returns true if and only if the statements/conditions evaluates true 
print((3>1) and (7>6))

#Logical OR:It evaluates to true if one of the statements or condition is true 
print((3>1) or (7>6))

#Logical NOT: it is used to negate a statement/ a condition
print(not(90>70) )