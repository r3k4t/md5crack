#Author : RKT 

import os
import sys
import hashlib
import time # This module import only for the calculation of exce time.

counter = 1 # counte the no of trying password.

md5_pass = raw_input("Enter md5 password :") # Here enter your hash password.
md5_file = raw_input("Enter Wordlist directory : ")# wordlist file directory.

#write try execpt block for handle execption
try :              
  md5_file = open(md5_file,'r') # file will read.
except :
  print ("\nFile Not Found") # if file location entered is wrong.
  quit()



#write for loop which is use for matching the hash password with wordlist password.
for password in md5_file:
  hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest() 
  start = time.time()
  print ("[*] Cracking  %d trying password :---->> %s"% (counter,password.strip()))
  counter += 1
  end = time.time()
  t_time = end - start

  if hash_obj == md5_pass:
      print("Password Found !!! password is : %s " % password)
      print("Total Runing Time : " ,t_time,"seconds")
      time.sleep(10)
      break

else:
  print ("Password Not Found")
