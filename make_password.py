
import string
import random
import os

def make_password():
  #Make a list of characters to use for passwords
  characters = string.ascii_letters + string.digits + string.punctuation

  #Get info from the user 
  site_app = input("What site or app are you making a password for?")
  os.system("clear")

  user_name = input("What is your username for the site or app?")
  os.system("clear")
  valid_set = [8,9,10,11,12,13,14,15,16]
  
  while True: 
    try: 
      length = int(input("How long do you want your password? max character 16 and minimum 8\n"))
      if length in valid_set  :
        break
      else:
        raise KeyError
    except KeyError:
      print("Sorry invalid character length, please try again.")
    
  #Generate the password 
  password = ""
  while length > 0:
    password = password + random.choice(characters)
    length -=1
  
  with open("passwords.txt", "a") as fobj:
    print(site_app, file=fobj)
    print(user_name, file=fobj)
    print(password, file=fobj)
    print("", file=fobj)
    print("", file=fobj)
  
  print("Your password was created successfully.")
  print(f"Your password for {site_app} is:\n {password}")
  input("Press enter to return to the main menu.")
  os.system("clear")
