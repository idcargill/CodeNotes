def concatenate(*args):
  word = args[0]
  for i in args:
    if (i != word[0]):
      word = F'{word}-{i}'
      print(i)
  return word

print(concatenate("I", "love", "Python", "!"))