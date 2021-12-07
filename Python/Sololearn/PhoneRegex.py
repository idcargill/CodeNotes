import re

regex = r'[189][0-9]{7}$'

# test = str(81239870)
test = str(81234567)

result = re.match(regex, test)

if result:
  print('Valid')
else:
  print('Invalid')


# findall   returns a list of all matches
# search    returns a match object for any match in str
# split     returns a list from string
# sub       replaces match with string