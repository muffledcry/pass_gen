#This is empty for nowh
import os
 
def show_password():
  with open("passwords.txt") as fobj:
     lines = fobj.readlines()
  # print(lines)
  sanitized = []
  for line in lines:
    if line == '\n':
      continue
    else:
      line = line.strip()
      # sanitized.append(line)
      for i in range(0, len(line), 3):
        print(line)


  password_dict = {sanitized[i]:{"username":sanitized[i + 1], "password": sanitized[i + 2]} for i in range(0, len(sanitized), 3)}

  #for values in :
  # print(password_dict)
""""
- make it look neat




"""
  

 


    