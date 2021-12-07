'''
- Strings are immutable
- same slicing as lists
- convert to unicode with u'words'
'''

### String Methods

s = 'kitten'

s.lower()
s.upper()
s.strip() # removes whitespace from start and end
s.isalpha()
s.isdigit()
s.isspace()
s.find('other string')  # returns first index or -1
s.replace('old', 'new')
s.split('delim')  # returns a list of substring separated by delimiter. returns list
s.join(list)  # opposite of split.  Joins a list into strings


# convert to unicode
ustring = u'words of stuff'

# convert to utf-8
s = ustring.encode('utf-8')