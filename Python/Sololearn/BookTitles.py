file = open("books.txt", "r")
books = file.readlines()

for b in books:
  first = b[0]
  b = b.replace('\n','')
  if len(b) > 0:
    length = str(len(b))
    print(first+length)


file.close()