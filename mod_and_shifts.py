#Ms. Liu
#7th Grade Computer Science
#Coding Activity 7
#3/18/24

def convert_minute_to_time(minutes):
  hours = round(minutes / 60)
  remaining_minutes = round(minutes % 60)
  return hours, remaining_minutes
def shift_letter(character, shift):
  result = chr(ord(character) + shift)
  return result


# Test the function
total_minutes = int(input("How many minutes do you want to convert to hour, mins?"))
hours, minutes = convert_minute_to_time(total_minutes)
print("Hours:", hours)
print("Minutes:", minutes)

character = input("Enter a character: ")
shift = int(input("Enter the shift value: "))
print("The characted after shifting is:", shift_letter(character, shift))