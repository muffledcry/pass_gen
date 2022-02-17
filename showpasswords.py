#This is empty for nowh
import os
 
def show_password():
  with open("passwords.txt") as fobj:
     lines = fobj.readlines()
  count = 0
  for line in lines:
    count+=1
    line = line.strip()
    print(line)

""""
- make it look neat

"""
  

 


    