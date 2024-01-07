#Ms. Liu
#7th Grade Computer Science
#Python Review Activity Answer Key
#Jan 7 2024
import math
def mathOperPrac1():
  #One day on Jupiter is 10 hours. 
  #Write a program that calculates how many days pass on Jupiter in one Earth year? 
  #Assume one Earth Year is 365.25 days
  JepDay = 10
  EarthYr = 365.25
  EarthDay = 24
  EarthHour = EarthYr * EarthDay
  Ans = EarthHour/JepDay
  print("The number of days Jupiter passed in a year on Earth is: " + str(Ans))
  print()

def mathOperPrac2():
  #Write a program to find the difference between a Sphere's volume and Surface Area 
  #given a radius of 3.
  #Hint: Answer should be zero
  #Hint: Use math.pi for pi
  #Hint: Use math.pow(x,y) for x to the power of y
  #Hint: the formula for volume is 4/3 * pi * r^3 
  #the formula for surface area is 4 * pi * r^2

  pi = 3.14
  radius = 3
  volume = 4/3 * pi * radius ** 3
  surface_area = 4 * pi * radius ** 2
  diff = round(volume - surface_area)
  print("The difference between a Sphere's volume and Surface Area with a radius of 3 is " + str(diff))
  print()

def mathOperPrac3():
  #Every year the population of rabbits on an island increases by 35%. 
  #This year there are 200 rabbits on the isalnd. How many will be there after 3, 5 and 10 years?
  rate_of_inc = 0.35
  ini_popl = 200
  year3popl = round(ini_popl*(1+rate_of_inc)**3)
  year5popl = round(ini_popl*(1+rate_of_inc)**5)
  year10popl = round(ini_popl*(1+rate_of_inc)**10)
  print("Third year's population will be " + str(year3popl))
  print("Fifth year's population will be " + str(year5popl))
  print("10th year's population will be " + str(year10popl))
  print()

def conversionPrac1():
  #Write a program that converts a person's height in inches to centimeters
  #and their weight in pounds to kilograms. 
  #Note: One inch is 2.54 centimeters and one pound is 0.453592 kilograms.
  #Hint: Use the input function to get the user's input
  #Hint: Use the int() function to convert the user's input to an integer
  #Hint: Use the str() function to convert the user's input to a string
  #Hint: Use the round() function to round the user's input to the nearest hundredth
  #Hint: Use the print() function to print the user's input
  inches = int(input("Enter your height in inches: "))
  pounds = int(input("Enter your weight in pounds: "))
  cm = inches * 2.54
  kg = round(pounds * 0.453592,2)
  print("Your height in centimeters is " + str(cm) + "cm")
  print("Your weight in kilograms is " +
       str(kg) + "kg")

def conditionalPrac():
  #Write a program that asks the user to enter a number for their grade
  #Output the letter grade that corresponds to the number entered
  #A+ = 97-100, A = 93-96, A- = 90-92
  #B+ = 87-89, B = 83-86, B- = 80-82
  #C+ = 77-79, C = 73-76, C- = 70-72
  #D = 60-69, F = 0-59
  #Make sure the user can input decimals too, round the numbers
  #Hint: Use the float() function to convert the user's input to a float
  #Hint: Use the round() function to round the user's input to the nearest hundredth
  number_grade = float(input("Enter your grade between 1-100: "))
  if number_grade > 100 or number_grade < 0:
    print("Invalid grade")
    return
  number_grade = round(number_grade, 2)
  letter_grade = ""
  if number_grade >= 97:
    letter_grade = "A+"
  elif number_grade >= 93:
    letter_grade = "A"
  elif number_grade >= 90:
    letter_grade = "A-"
  elif number_grade >= 87:
    letter_grade = "B+"
  elif number_grade >= 83:
    letter_grade = "B"
  elif number_grade >= 80:
    letter_grade = "B-"
  elif number_grade >= 77:
    letter_grade = "C+"
  elif number_grade >= 73:
    letter_grade = "C"
  elif number_grade >= 70:
    letter_grade = "C-"
  elif number_grade >= 60:
    letter_grade = "D"
  else: letter_grade = "F" 
  print("Your grade is: " + letter_grade)
  
mathOperPrac1()
mathOperPrac2()
mathOperPrac3()

conversionPrac1()
conditionalPrac()