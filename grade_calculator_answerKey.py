  #Ms. Liu
  #7th Grade Computer Science
  #Python Review Activity Answer Key
  #Jan 7 2024

  #Write a program that asks the user to enter a number for their grade
  #Output the letter grade that corresponds to the number entered
  #A+ = 97-100, A = 93-96, A- = 90-92
  #B+ = 87-89, B = 83-86, B- = 80-82
  #C+ = 77-79, C = 73-76, C- = 70-72
  #D = 60-69, F = 0-59
  #Make sure the user can input decimals too, round the numbers
  #Hint: Use the float() function to convert the user's input to a float
  #Hint: Use the round() function to round the user's input to the nearest hundredth
  def conditionalPrac():
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