## 4 ways to reverse a list

# Revese Method
sample_1 = [1, 2, 3, 4]
sample_1.reverse()
# print(sample_1)



# For Loop Reverse
sample_2 = [1, 2, 3, 4]
sample_2_new = []
n = len(sample_2) -1

for i in range(len(sample_2)):
  sample_2_new.append(sample_2[n])
  n -= 1
# print(sample_2_new)

sample_3 = [1, 2, 3, 4]
print(sample_3[::-1])

# sample_4 = [1, 2, 3, 4]


def reverse_list(lst):
  # stop half way needed
  n = len(lst)
  for i in lst:
    lst[i] = lst[n]
    n -= 1
    i += 1
  return n

