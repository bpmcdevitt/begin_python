#!/usr/bin/env python3

x = input('Input your temperature in celsius: ')

f = 'Fahrenheit'
k = 'Kelvin'
r = 'Rankine'

def celsius_to_farenheit(x):
    x = float(x)
    return ((x * 1.8) + 32.0)

results = celsius_to_farenheit(x)

print("you entered: {}".format(x))
print("the converted value is {}".format(results))




