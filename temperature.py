#!/usr/bin/env python3

x = input('Input your temperature in celsius: ')

def celsius_to_farenheit(x):
    x = float(x)
    return ((x * 1.8) + 32.0)

def celsius_to_kelvin(x):
    x = float(x)
    return (x + 273.15)

def celsius_to_rankine(x):
    x = float(x)
    return ((x * 1.8) + 491.67)
def celsius_to_romer(x):
    x = float(x)
    return ((x * 0.252) + 7.5)


results = celsius_to_farenheit(x)
results1 = celsius_to_kelvin(x)
results2 = celsius_to_rankine(x)
results3 = celsius_to_romer(x)

print("You entered: {}".format(x))
print("The converted value is {} in Farenheit".format(results))
print("The converted value is {} in Kelvin".format(results1))
print("The converted value is {} in Rankine".format(results2))
print("The converted value is {} in Romer".format(results3))




