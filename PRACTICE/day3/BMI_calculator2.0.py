#CHALLENGE3 
# BMI calculator2.0. 
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
BMI = round(weight/height**2)
if BMI < 18.5:
    print(f"Your bmi is {BMI}, you are underweight")
elif BMI < 25:
    print(f"Your bmi is {BMI}, you are normalweight")
elif BMI < 30:
    print(f"Your bmi is {BMI}, you are overweight")
elif BMI < 35:
    print(f"Your bmi is {BMI}, you are obese")
else:
    print(f"Your bmi is {BMI}, you are clinically obese")

