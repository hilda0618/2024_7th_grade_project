#Ms. Liu
#7th Grade Computer Science
#Caesar Cipher Program Solution
#March 20, 2024

'''Program Description:
Caesar Cipher program will ask for a user input and the key they want to shift
And encrypt/decrypt accordingly

The program should not encrypt/decrypt 
any non-alphabetical characters including spaces and numbers

The program should encrypt/decrypt uppercase and lowercase letters'''

option = input("Do you want to encrypt or decrypt?").casefold()
result = ""
SPECIALCHARACTERS = "[@_!#$%^&*()<>?/\|}{~:],."
message = input("What is your message?")
if option == "encrypt":
  key = int(input("How many places do you want to shift?"))
  for letter in message:
    #Don't encrypt space or special character or number
    if letter == " " or letter in SPECIALCHARACTERS or letter.isdigit():
      result += letter
    elif (letter.isupper()):
      result += chr((ord(letter) + key - ord("A")) % 26 + ord("A"))
    # Encrypt lowercase characters in plain text
    else:
      result += chr((ord(letter) + key - ord("a")) % 26 + ord("a"))
  print(result)

else:
  key = int(input("How many places do you want to shift back?"))
  for letter in message:
    #Don't decrypt space or special character or number
    if letter == " " or letter in SPECIALCHARACTERS or letter.isdigit():
      result += letter
    elif (letter.isupper()):
      result += chr((ord(letter) - key - ord("A")) % 26 + ord("A"))
      # Encrypt lowercase characters in plain text
    else:
      result += chr((ord(letter) - key - ord("a")) % 26 + ord("a"))
  print(result)


