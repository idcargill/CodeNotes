# read
with open('sample_text.txt', 'r') as reader:
  all_text = reader.read()
  print(all_text)

# readlines  
with open('sample_text.txt', 'r') as reader:
  lines = reader.readlines()
  for i in lines:
    print(i)
  
# append with read a+  or r+
with open('sample_text.txt', 'a+') as reader:
  reader.write('\nNew Text with r+')
  text = reader.read()
  print(text)
