#Ms. Liu
#7th Grade Computer Science
#Python Review Activity Answer Key
#Jan 7 2024
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
  #Hint: Use 3.14 for pi
  #Hint: Use x**y for x to the power of y
  #Hint: the formula for volume is 4/3 * pi * r^3 
  #Hint: the formula for surface area is 4 * pi * r^2
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

mathOperPrac1()
mathOperPrac2()
mathOperPrac3()