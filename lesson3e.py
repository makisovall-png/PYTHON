# Below is a grading system based on what a student would have gotten
marks = int(input("Enter students marks:"))
#print("The entered marks is ", marks)
if marks < 30 and marks >0:
    print("below average")
if marks >=30 and marks < 40:
    print("average")
if marks >=40 and marks >=70:
    print("above average")
elif marks >=70 and marks<=100:
    print("excellent ")
else:
    print("invalid input")