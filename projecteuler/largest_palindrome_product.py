# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
  strng = str(num)
  str_len = len(strng)
  for i in range(int(str_len/2)+1):
    if strng[i] != strng[str_len-i-1]:
      return False
  return True

def largest_palindrome_product(num):
  highest_n_digit = int(num * str(9))
  lowest_n_digit = 10 ** (num-1)
  max_num = 0
  for i in range(highest_n_digit,lowest_n_digit+1,-1):
    for j in range(i,lowest_n_digit+1,-1):
      num = i*j
      if(is_palindrome(num)):
        max_num = num if num > max_num else max_num
  
  return max_num
  
def main():
  num = int(input("Please enter a number digits to find the larges palindrome product :"))
  print(largest_palindrome_product(num))

if __name__ == '__main__':
  main()
