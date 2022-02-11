#Travis, Pedro, Hassana, Gabe, Rogerson, Guychara
import os


from make_password import make_password
from change_password import change_password

print("Welcome to Password Generator!")
print("")

def menu():
  print("What would you like to do?\n- Enter 1 to Generate a New Password\n- Enter 2 to Change a Password\n- Enter 3 to View A Password")

  user_choice = int(input())
  os.system("clear")

  if user_choice == 1:
    make_password()
    menu()
  elif user_choice == 2:
    change_password()
    menu()
  elif user_choice == 3:
    pass
  else:
    pass

menu()