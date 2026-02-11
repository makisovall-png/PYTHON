#Question1
def calculate_area():
    length = 10
    width = 5 
    area = length * width
    print(f"The area of the rectangle with length{length} and width{width} is:", area)
calculate_area()

#Question two 
def arithmetic_operations(num1, num2):
    if num2 == 0:
        division_result = "Undefined(division by zero)"
    else:
        division_result = num1 / num2 
    results ={
        'sum': num1 + num2,
        'difference': num1 - num2,
        'product': num1 * num2,
        'division': division_result
    }
    return results

#Question Three
def check_numbers():
    num = int(input("enter a number"))
        if num > 0:
            print(f("{num} is a positive number"))
        elif num < 0:
            print(f"{num} is a negative number")
        else:
            print(f"the number is zero")

#Question four 