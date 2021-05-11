from colorama import Fore, Back, Style

def errorColor(message):
  print(Fore.RED + message, end='')
  print(Style.RESET_ALL)

def successColor(message):
  print(Fore.GREEN + message, end='')
  print(Style.RESET_ALL)

def RecommendColor(message):
  print(Fore.YELLOW + message, end='')
  print(Style.RESET_ALL)