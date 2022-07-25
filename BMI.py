#!/usr/bin/env python3

def calculate_bmi(weight, height):
    weight = float(weight)
    height = float(height)
    return((weight/(height/100)) / (height/100))

def convert_lb_to_kg(lb):
    lb = float(lb)
    return(lb * 0.45)

def convert_ft_to_inches(ft, inches):
    ft = float(ft)
    ft_inches = (ft * 12.0)
    eq = ft_inches + float(inches)
    return(int(eq))

def convert_inches_to_cm(inches):
    inches = float(inches)
    return(inches * 2.54)

def convert_ft_to_cm(ft, inches):
    inches = convert_ft_to_inches(ft, inches)
    cm = convert_inches_to_cm(inches)
    return cm
    

a = input("Do you know your weight in kilogram? ")

if a == 'no':
    print("Please input your weight: ")
    lb = input("How many pounds do you weight? ")
    resultweight = convert_lb_to_kg(lb)
    print("You weight in kilogram is {}".format(resultweight))
elif a == 'yes':
    weight = input("Please input your weight in kilogram: ")
    resultweight = weight
else:
    print("You did not answer 'yes' or 'no' to my questions. Goodbye.")
    exit()

b = input("Do you know your height in centimeter? ")

if b == 'no':
    print("Please input your height: ")
    ft = input("How tall are you in feet? ")
    inches = input("How tall are you in inches? ")
    result_cm = convert_ft_to_cm(ft, inches)
    print("Your height in cm is {}".format(result_cm))
elif b == 'yes':
    result_cm = input("Please input your height in cm: ")
else:
    print("You did not answer 'yes' or 'no' to my questions. Goodbye.")
    exit()

#weight = input("Please input your weight in kilogram: ")
#height = input("Please input your height in centimeter: ")
result = calculate_bmi(resultweight, result_cm)

print("Your height entered {} in centimeter (cm)".format(result_cm))
print("Your weight entered {} in kilogram (kg)".format(resultweight))
print("Your BMI is {}".format(result))


