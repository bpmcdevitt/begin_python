#!/usr/bin/env python
message = 'Hello World'

#print(len(message))
print(message[0:5])
#print(message.lower())
#print(message.upper())
#print(message.count('W'))
#print(message.find('World'))

#new = message.replace('World', 'Universe')
#message=message.replace('World', 'Universe')

#print(message)
#print(new)
#-----------------------------------------------------------------

#greeting = 'Hello'
#name = 'Muay'
#message = greeting + ', ' + name+'. Welcome!'
#message = '{}, {}. Welcome!'.format(greeting, name)

#print(help(str.lower))
#------------------------------------------------------------------

#num = 4.5
#print(type(num))

#print(3*(2+1))

#num = 1
#num+=10
#print(num)

#print(abs(-3))
#print(round(3.75, 1))

#num1 = 3
#num2 = 2
#print(num1 == num2)

#num1 = '100'
#num2 = '200'

#num1 = int(num1)
#num2 = int(num2)
#print(num1 + num2)
#------------------------------------------------------------------

#courses = ['History', 'Math', 'Physics', 'CompSci']
#nums = [1, 5, 2, 4, 3]
#courses2 = ['Art', 'Education']

#course_str = ', '.join(courses)
#newlist = course_str.split(', ')
#print(course_str)
#print(newlist)

#courses.append('Art')
#courses.insert(0, 'Art')
#courses.insert(0, courses2)
#courses.extend(courses2)
#courses.remove('Math')
#courses.pop()
#popped = courses.pop()
#courses.reverse()
#courses.sort(reverse=True)
#nums.sort(reverse=True)
#sorted(courses)
#sorted_courses = sorted(courses)

#print(courses.index('Physics'))
#for item in courses:   #loop
    #print(item)
#for index, item in enumerate(courses, start=1):
    #print(index, item)
    #print('Math' in courses)
#print(sorted_courses)
#print(sum(nums))  #max,min,sum
#print(popped)
#print(courses[2:])
#print(len(courses))
#-------------------------------Key-Value-Pairs---------------------------------

student = {'name': 'John', 'age': '25', 'courses': ['Math', 'CompSci']}


print(student['courses'])
