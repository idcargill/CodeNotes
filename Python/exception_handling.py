# Syntax errors stop all code

# TypeErrors stop code at error

try:
  pass
except:
  pass
else:
  pass
finally:
  pass


x = 10
try:
  if x > 100:
    print('Yay!')
  else:
    raise Exception('My custom Error message!')
  print(y)
except Exception as e:
  print('Catching an exception: ', e)
  print('Handling error catch')
finally:
  print('I always print')

# else runs if no exception triggers
try:
  print('cats')
except Exception as e:
  print(e)
else:
  print('else this stuff')
finally:
  print('I always run')