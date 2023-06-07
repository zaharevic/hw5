def Sum(num1,num2):
    if(num2 == 0):
        return num1
    else:
        return Sum(num1 + 1, num2 - 1)


print(Sum(int(input()),int(input())))