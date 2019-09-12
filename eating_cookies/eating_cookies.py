

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n):

  possible_combinations = 0

  if n < 1:
    possible_combinations = 0
    return possible_combinations
  
  if n == 1:
    possible_combinations = 1
    return possible_combinations
  
  if n == 2:
    possible_combinations = 2
    return possible_combinations

  if n == 3:
    possible_combinations = 4
    return possible_combinations 

  if n > 3:
    first_num = eating_cookies(n-1)
    second_num = eating_cookies(n-2)
    third_num = eating_cookies(n-3)

    possible_combinations = first_num + second_num + third_num
    return possible_combinations

print(eating_cookies(5))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')