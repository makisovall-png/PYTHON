number = 100
answer = number / 0
print(answer)
#On the try block: You can run some codes/ statements and if it successful the try block will get executed other the except block will be executed when the anticipated
try:
    number = 100
    answer = number / 0
except Exception as e:
    print("the answer is:",e)