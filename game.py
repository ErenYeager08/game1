import random
from colorama import init, Fore

init()
# n = False
# n1 = input("yes or no: ")
# if(n1 == "yes"):
#     n == True

# s = int(input(""))
# d = 0
while(True):
    ran = random.randint(1,5)
    num2 = int(input(Fore.WHITE + "Tell me the number you're thinking of: "))
    if (ran == num2):
        print(Fore.GREEN + f"success, randon number {ran}")
    else:
        print(Fore.RED + f"you lose!!, randon number {ran}")
    print(Fore.WHITE + "Do you wanna keep playing?\ny(Yes)\nn(No)")
    res = input(":")
    if (res == "y"):
        continue
    elif(res == "n"):
        break
