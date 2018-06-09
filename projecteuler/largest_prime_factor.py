# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math

def prime_factors(num):
  prime_factors = ''

  if(num%2 == 0):
    prime_factors = f'{prime_factors}2, '
    num = num / 2
  
  for i in range(3,int(math.sqrt(num))+1, 2):
    if(num%i == 0):
      prime_factors = f'{prime_factors}{i}, '
      num = num / i
  
  return prime_factors

def main():
  num = int(input("Please enter a number to find its prime factors :"))
  print(prime_factors(num))

if __name__ == '__main__':
  main()
