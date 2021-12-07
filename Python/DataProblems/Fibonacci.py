''''
The Fibonacci sequence is one of the most famous formulas in mathematics.
Each number in the sequence is the sum of the two numbers that precede it.
For example, here is the Fibonacci sequence for 10 numbers, 
starting from 0: 0,1,1,2,3,5,8,13,21,34.

Write a program to take N (variable num in code template) positive numbers as input, 
and recursively calculate and output the first N numbers of the Fibonacci sequence 
(starting from 0).
'''


def fibonacci(n):
  if n <= 1:
    return n
  else:
    print(fibonacci(n-1) + fibonacci(n-2)) 
    return fibonacci(n-1) + fibonacci(n-2) 

# for i in range(6):
#   print(fibonacci(i))

fibonacci(10)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34




# Fibonacci 
# geekforgeek recursion

def fib(n):
  
  # Stop Condition
  if (n == 0):
    return 0
  
  # stop condition
  if (n == 1 or n == 2):
    return 1
  
  # Recursion Function
  else :
    return fib(n-1) + fib(n-2)


n = 5
print("Fibonacci series of 5 numbers is :",end=" ")

# for i in range(0 , n):
#   print(fib(i), end=' ')