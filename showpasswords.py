#This is empty for nowh
import os
 
def show_password():
  with open("password.txt") as fobj:
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


    