#!/usr/bin/env python3

x = input("Please input your weight in kilogram: ")
y = input("Please input your height in centimeter: ")

def calculate(x, y):
    x = float(x)
    y =float(y)
    return((x/(y/100)) / (y/100))

result = calculate(x, y)

print("Your height entered {} in centimeter (cm)".format(x))
print("Your weight entered {} in kilogram (kg)".format(y))
print("Your BMI is {}".format(result))


