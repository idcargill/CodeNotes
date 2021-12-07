
# A Python 3 program to
# demonstrate working of
# recursion
 
 
def printFun(test):
 
    if (test < 1):
        return
    else:
 
        print(test, end=" ")
        printFun(test-1)  # statement 2
        print(test, end=" ")
        return
 
# Driver Code
test = 4
# printFun(test)


####
# Fibonacci 

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

for i in range(0 , n):
  print(fib(i), end=' ')