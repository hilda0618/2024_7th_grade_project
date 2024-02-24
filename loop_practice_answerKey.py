#Ms. Liu
#7th Grade Computer Science
#Python Review Activity Answer Key
#Jan 7 2024

# Display each letter of the word on a new line using a loop
def loopPractice():
    word = input("Enter a word: ")
    print("Each letter of the word:")
    for letter in word:
        print(letter)

#Ask for user input and reverse the word
def loopPractice2():
  word = input("Enter a word: ")
  reverse = ""
  for letter in word:
    reverse = letter + reverse
  print("The reverse of this word is: " + reverse)