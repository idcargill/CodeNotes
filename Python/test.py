dice_rolled = [1, 5, 5, 4, 3, 1]

user_input = '11555'
valid_entries = []
string = ''

def validate_input(user_input, dice_rolled):

  try:
    user_choice = [int(i) for i in user_input]

    for i in user_choice:
      user_count = user_choice.count(i)
      dice_count = dice_rolled.count(i)
      if user_count <= dice_count:
        valid_entries.append(i)
    return string.join([str(item) for item in valid_entries])
  except Exception as e:
    return 'Invalid input, try again'

x = validate_input(user_input, dice_rolled)
print(x)
