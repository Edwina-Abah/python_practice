#CHALLENGE2B------create an IBMI calculator.   request for users weight, and height using the IBM formula---let the output be in whole number.
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
###########################################
###########################################
IBM = int(weight/height**2)
print(IBM)
