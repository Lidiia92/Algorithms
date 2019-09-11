

import argparse

prices = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):
  
  current_min_price_so_far = 0
  max_profit_so_far = 0
  profits= []


  for i in range(0, len(prices) - 1):
    current_min_price_so_far = prices[i]
  
    for j in range (1, len(prices) - 1):
      profits.append(prices[j] - current_min_price_so_far)

  max_profit_so_far = profits[0]


  for n in range(1, len(profits)):

    if profits[n] > max_profit_so_far:
      max_profit_so_far = profits[n]
      

      
  return max_profit_so_far

print(find_max_profit(prices))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))