#Ms. Liu
#7th Grade Computer Science
#Password Program Answer Key
#Jan 8 2024
#Password program will ask for a password and check against a set of rules.
#It will repetitively ask for a password until all rules are met.

#The first two rules have been programmed.  Now, it's your turn to program each rule from #3 to #7.

#Rules:
#1. At least 12 characters
#2. Should have numbers
#3. Should have special characters
#4. Capital letters
#5. Lower case letters
#6. Should not include your name
#7. Should not have the word password
#Create two additional rules of your own.

#static variable
TOTAL_NUMBER_OF_RULES = 7 #total number of rules going to be checked
NUMBERS = "0123456789"
SPECIALCHARACTERS = "!@#$%^&*()"
NAME = "Hilda"
PASSWORD = "Passowrd"

rulesMet = 0 #count the number of rules met by the password given

#Rule 1. At least 12 characters
def rule1(password):  
  if len(password)>=12:
      print("Good work!  Your password has enough characters.")
      return True
  else:
      print("It's too short! Has to contain at least 12 characters")
      return False
    
#Rule 2. Should have numbers
def rule2(password):
  rulesMet = False 
  for n in NUMBERS:
      if n in password:
          print("Good work!  Your password contains a number.")
          rulesMet = True
          return rulesMet
  #if found == False:
  print("Your password does not contain a number.")
  return rulesMet

#Rule 3. Should have special characters
def rule3(password):
  rulesMet = False 
  for n in SPECIALCHARACTERS:
    if n in password:
        print("Good work!  Your password contains a special character.")
        rulesMet = True
        return rulesMet
  #if found == False:
  print("Your password does not contain a special character.")
  return rulesMet

#Rule 4. Has Capital letters
def rule4(password):
  rulesMet = False 
  for n in password:
    if n.isupper():
        print("Good work!  Your password contains an upper case letter.")
        rulesMet = True
        return rulesMet
  #if found == False:
  print("Your password does not contain an upper case letter.")
  return rulesMet
  
#Rule 5. Lower case letters
def rule5(password):
  rulesMet = False 
  for n in password:
    if n.islower():
        print("Good work!  Your password contains a lower case letter.")
        rulesMet = True
        return rulesMet
  #if found == False:
  print("Your password does not contain a lower case letter.")
  return rulesMet

#Rule 6. Should not include your name
def rule6(password):
  rulesMet = False 
  password = password.casefold()
  if NAME.casefold() in password:
    print("Your password contains your name.")
    return rulesMet
  #if found == False:
  print("Good work!  Your password does not contain your name.")
  rulesMet = True
  return rulesMet
  
#Rule 7. Should not have the word password
def rule7(password):
  rulesMet = False 
  password = password.casefold()
  if PASSWORD.casefold() in password:
    print("Your password contains the word 'password'.")
    return rulesMet
  #if found == False:
  print("Good work!  Your password does not contain the word 'password'.")
  rulesMet = True
  return rulesMet
  
while rulesMet != TOTAL_NUMBER_OF_RULES:
    password = input("Please give me a password: ")
    rulesMet = 0 #reset the number of rules met

    #rule 1
    if rule1(password):
        rulesMet += 1 #rulesMet = rulesMet + 1
    #rule 2
    if rule2(password):
      rulesMet += 1
    #rule 3
    if rule3(password):
      rulesMet += 1
    #rule 4
    if rule4(password):
      rulesMet += 1
    #rule 5  
    if rule5(password):
      rulesMet += 1
    #rule 6  
    if rule6(password):
      rulesMet += 1  
    #rule 7 
    if rule7(password):
      rulesMet += 1  
if rulesMet == 7:
  print("Good work!  You have met all of the rules!")