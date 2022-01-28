import time

def insert_list(num):
  start = time.perf_counter()
  insert_list = []
  for i in range(num):
    insert_list.insert(0, i)
  end = time.perf_counter()
  return f'insert in front: time in seconds: {end - start}'


def pop_list(num):
  start = time.perf_counter()
  pop_list = []
  for i in range(num):
    pop_list.append(i)
    for i in pop_list:
      pop_list.pop()
  end = time.perf_counter()
  return f'append_list: time in seconds: {end - start} {len(pop_list)}'

print(pop_list(100000))
print(insert_list(100000))