print("Welcome to the BMI Calculator! Simply enter your height and weight to find out your BMI")
print("\n")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / height ** 2
BMI = int(round(BMI))
print("\n")
if BMI < 18.5 :
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25 :
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI < 30 :
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI < 35 :
    print(f"Your BMI is {BMI}, you are obese")
else :
    print(f"Your BMI is {BMI}, you are clinically obese")