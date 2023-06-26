#prints message on terminal and waits for user to input data
name = input('What is your name? ')
favcolor = input('What is your favorite color? ')
print (name + ' likes ' + favcolor)

birth_year = input('Birth year:')
age = 2023- int(birth_year)
print(age)

print(type(birth_year))
print(type(age))

weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print (weight_kg)

course = "Pythons's Course for Beginners"
print(course)

course = '''Hi John,
great job

the support team'''
print(course)

course = 'Python for Beginners'
print(course[-2])
#result  r                  *
course = 'Python for Beginners'
#         0123
print(course[0:3])
#result  Pyt