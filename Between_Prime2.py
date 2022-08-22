
def between_prime(upp,low=0):
  print('The prime numbers between {} and {} are: '.format(low,upp), end=' ')
  for i in range(low, upp+1):
    if i > 1:
      for j in range(2, i):
        if (i % j) == 0:
          break
      else:
        print(i, end=" ")

between_prime(low=12,upp=25)
