
def between_prime1():
  x = int(input('Enter the lower range :'))
  y = int(input('Enter the upper range :'))
  print('The prime numbers between the range are: ', end=' ')
  for i in range(x,y+1):
    if i > 1:
      for j in range(2, i):
        if (i % j) == 0:
          break
      else:
        print(i, end=" ")

between_prime1()
