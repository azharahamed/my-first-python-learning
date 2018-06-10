# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without 
# any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_number_divisible_by(lower,upper):
  number = 1
  while True:
    divisible_by_all = True
    for j in range(lower,upper+1):
      if number%j !=0:
        divisible_by_all = False
    if divisible_by_all:
        return number
    number = number+1
    
  if lowest < max+1:
    return lowest

def main():
  num = int(input("Please enter the limit "))
  print(smallest_number_divisible_by(1,num))
  
if __name__ == '__main__':
  main()