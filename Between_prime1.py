
def between_prime():
  x = int(input('Enter a number :'))
  print('The prime numbers between the range are: ', end=' ')
  for i in range(0,x+1):
    if i > 1:
      for j in range(2, i):
        if (i % j) == 0:
          break
      else:
        print(i, end=" ")

between_prime()
