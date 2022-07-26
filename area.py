#!/usr/bin/env python3

def cal_square(length):
    length = float(length)
    return(length * length)

def cal_rectangle(width, length):
    return(float(width) * float(length))

def cal_triangle(width, length, height):
    return(float(width) * float(length) * float(height))

def cal_circle(radius):
    return(3.14 * (float(radius) * float(radius)))

x = input("Please select your area that you want to calculate. \n A) Square \n B) Recgtangle \n C) Triangle \n D) Circle \n ")

if x == "A":
    length = input("Please input your length: ")
    result_square = cal_square(length)
    print("Your area is {} ".format(result_square))
elif x == "B":
    width = input("Please input your width: ")
    length = input("Please input your length: ")
    result_rectangle = cal_rectangle(width, length)
    print("Your area is {} ".format(result_rectangle))
elif x == "C":
    width = input("Please input your width: ")
    length = input("Please input your length: ")
    height = input("Please input your height: ")
    result_triangle = cal_triangle(width, length, height)
    print("Your area is {} ".format(result_triangle))
elif x == "D":
    radius = input("Please input your radius: ")
    result_circle = cal_circle(radius)
    print("Your area is {} ".format(result_circle))   
else:
    print("You did not select the choice in the lists that I provide you. Please run and select it again!")
    exit()

