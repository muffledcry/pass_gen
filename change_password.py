import os, random, string


def change_password():
  with open("passwords.txt") as fobj:
    lines = fobj.readlines()



  sanitized = []
  for line in lines:
    if line == '\n':
      continue
    else:
      line = line.strip()
      sanitized.append(line)


  password_dict = {sanitized[i]:{"username":sanitized[i + 1], "password": sanitized[i + 2]} for i in range(0, len(sanitized), 3)}
  


  print("You have passwords for the following sites and apps: ")
  apps_sites = password_dict.keys()


  for app in apps_sites:
    print(f"{app}")
  
  account = input("Which password would you like to change?")

  length = int(input("How long do you want your password?"))
  os.system("clear")

  characters = string.ascii_letters + string.digits + string.punctuation

  password = ""
  while length > 0:
    password = password + random.choice(characters)
    length -=1

  password_dict[account]["password"] = password
  print("Your password has been changed.")
  print("Your new password is:")
  print(password_dict[account]["password"])
  input("Press enter to return to the main menu.")
  os.system("clear")

  with open("passwords.txt", "w") as fobj:
    keys = list(password_dict.keys())
    
    for key in keys:
      print(key,file=fobj)
      print(password_dict[key]["username"], file=fobj)
      print(password_dict[key]["password"], file=fobj)
      print("", file=fobj)