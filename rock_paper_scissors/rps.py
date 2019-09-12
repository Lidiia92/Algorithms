

import sys

rps_array = ['rock', 'papper', 'scissors']

#combination_length is 1, 2, 3, etc

def rock_paper_scissors(combination_length):

  printAllCombinations(rps_array, "", combination_length)
  
def printAllCombinations(rps_array, prefix, combination_length):
  
  print ("\n NEW ITERATION")
      
  if (combination_length == 0) : 
      print('\n Combination of length N \n', prefix) 
      return
      
  for i in range(3): 
    
  # Next character of input added 
    newPrefix = prefix + rps_array[i] + " "
    print(f'\n prefix {prefix} newPrefix {newPrefix}')
        
    # combination_length is decreased, because  
    # we have added a new character 
    printAllCombinations(rps_array, newPrefix, combination_length - 1) 
    
print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')