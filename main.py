"""
Python terminal game (slot machine)
*******************************************************************************
Description:
This Python program represents a simple slot machine game in the terminal.
- Users start with 20 tokens.
- Each spin costs 2 tokens.
- Winning combinations result in token prizes:
    - 3 of the same symbols: 20 tokens
    - '$$$': 50 tokens
    - Matching symbols with a wildcard '?': 10 tokens
    - Two wildcards '??': 10 tokens
- Users can quit the game at any time by entering 'q'.
- The game continues until the user runs out of tokens or quits.

Note: This program uses ANSI escape codes for colored output in the terminal.
******************************************************************************
"""
#Import the random module.
import random

# ANSI escape codes for colors
BRIGHT_GREEN = '\033[92;1m'
BRIGHT_YELLOW = '\033[93;1m'
BRIGHT_BLUE = '\033[94;1m'
BRIGHT_MAGENTA = '\033[95;1m'
BRIGHT_CYAN = '\033[96;1m'
BRIGHT_RED = '\033[91;1m'

#Resets the previous color changes.
RESET = '\033[0m'

def print_message():
  """This function prints the greeting message and rules to the user"""
  #Print an initial greeting message.
  print(f"{BRIGHT_RED}Welcome to the Slot Machine game!{RESET}")
  print(f"{BRIGHT_YELLOW}See if luck is on your side as you spin and try to win tokens!{RESET}")
  
  #Print the Game Rules.
  print("*" * 50)
  print(f"{BRIGHT_CYAN}Game Rules: {RESET}")
  print("*" * 50)
  print("1. You start with 20 tokens.")
  print("2. Each spin costs 2 tokens.")
  print("3. If you get 3 of the same symbols, you win 20 tokens.")
  print("4. If you get '$$$', you win 50 tokens.")
  print("5. If two symbols match and the third symbol is a wildcard '?', you win 10 tokens.")
  print("6. If two symbols are wildcards '??', you win 10 tokens.")
  print("You can quit at any time by entering 'q'.")
  print("*" * 50)

def spins():
  """This function selects symbols at random from a list of symbols."""
  # Create a dictionary to map symbols to colors
  symbol_colors = {"$": BRIGHT_YELLOW, "7": BRIGHT_MAGENTA, "*": BRIGHT_GREEN, "?": BRIGHT_CYAN, "#": BRIGHT_RED, "!": BRIGHT_BLUE}
  
  #Create a list of possible slot machine symbols.
  slot_symbols = ["$", "7", "*", "?","#", "!"]
  symbol1 = random.choice(slot_symbols)
  symbol2 = random.choice(slot_symbols)
  symbol3 = random.choice(slot_symbols)
  #Print the symbols.
  print("-" * 50)
  print(f"{BRIGHT_BLUE}Spin Result: {RESET}| {symbol_colors[symbol1]}{symbol1}{RESET} | {symbol_colors[symbol2]}{symbol2}{RESET} | {symbol_colors[symbol3]}{symbol3}{RESET} |")
  print("-" * 50)
  return symbol1, symbol2, symbol3
  

def win_check(symb1,symb2,symb3):
  """This function checks if the user has won any tokens."""
  if symb1 == symb2 == symb3:
    if symb1 == "$":
      print(f"{BRIGHT_RED}Congratulations! You won 50 tokens!{RESET}")
      prize = 50
    else:
      print(f"{BRIGHT_RED}Congratulations! You won 20 tokens!{RESET}")
      prize = 20

  elif (symb1, symb2, symb3).count("?") == 2 or ("?" in (symb1, symb2, symb3) and (symb1 == symb2 or symb1 == symb3 or symb2 == symb3)):
    print(f"{BRIGHT_RED}Congratulations! You won 10 tokens!{RESET}")
    prize = 10
  else:
    print("Sorry. You didn't win.")
    prize = 0
    
  return prize
  
def slot_machine():
  """This function simulates a slot machine game."""

#Call print_message() function to greet the user.
print_message()
print()
# Initialize user's balance.
user_balance = 20

while True:

  # Check the user's balance before asking to spin:
  if user_balance < 2:
      print(f"Your balance is {user_balance}. You don't have enough money to spin." )
      print(f"{BRIGHT_GREEN}Game over. Thank you for playing!")
      break
  #Ask the user to start the game:
  print(f"Your balance is {user_balance} tokens. Each spin costs 2 tokens.")
  user_input = input("Type 's' to start the game, 'q' to quit: ")
  if user_input.lower()=='s':
    print("Goood luck!")
    #Deduct $2 from the user's balance for each spin.
    user_balance -= 2
    #Call the spins() function to simulate the slot machine spin.
    symbol1, symbol2, symbol3 = spins()
    #Call the win_check(symbol1,symbol2,symbol3) function to check if the user wins.
    result = win_check(symbol1, symbol2, symbol3)
    user_balance +=result
    
  elif user_input.lower() == 'q':
    print("*" * 50)
    print(f"{BRIGHT_GREEN}Game over. Your final balance is {user_balance} tokens. Thank you for playing!")
    break
    
slot_machine()

