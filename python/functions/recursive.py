# Fibonacci result
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

#fib(7) = fib(6) + fib(5) = 8 + 5 = 13
#fib(6) = fib(5) + fib(4) = 5 + 3 = 8
#fib(5) = fib(4) + fib(3) = 3 + 2 = 5
#fib(4) = fib(3) + fib(2) = 2 + 1 = 3
#fib(3) = fib(2) + 1 = 1 + 1 = 2
#fib(2) = 1 + 0  = 1
#fib(1) = 1
#fib(0) = 0


# Fibonnachi sequence
for i in range(7):
  print(fib(i))
  
  
  # Fibonnaci Iteration
  def iterFibo(n):
    a = 1
    b = 1
    if n == 1:
        print('0')
    elif n==2:
        print ('0', '1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range (n-3):
            total = a + b
            b = a
            a = total
            print(total)

iterFibo(8)
