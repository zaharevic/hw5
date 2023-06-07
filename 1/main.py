def Pow(number,degree):
    if degree > 1:
         return Pow(number, degree -1) * number
    else:
        return number

print(Pow(int(input()),int(input())))