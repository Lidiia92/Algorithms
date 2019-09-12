

import sys

rps_array = ['rock', 'papper', 'scissors']
result_array = []

#combination_length is 1, 2, 3, etc

def rock_paper_scissors(combination_length):

  printAllCombinations(rps_array, "", combination_length)
  
def printAllCombinations(rps_array, prefix, combination_length):
  
  print ("\n NEW ITERATION")
      
  if (combination_length == 0) : 
      result_array.append(prefix.split(','))

      for i in range(len(result_array)):
        for j in range(len(result_array[i])):
          if result_array[i][j] == '':
            result_array[i].remove('')

      print(result_array)
      return result_array 
      
  for i in range(3): 
    
  # Next character of input added 
    newPrefix = prefix + rps_array[i] + ","

    printAllCombinations(rps_array, newPrefix, combination_length - 1) 
    
print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')