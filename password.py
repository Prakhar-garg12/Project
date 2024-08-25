'''
                              TASK 3

A password generator is a useful tool that generates strong and

random passwords for users. This project aims to create a
password generator application using Python, allowing users to

specify the length and complexity of the password.
'''

import string
import random

if __name__=="__main__":
    s1=string.ascii_uppercase
  
    s2=string.ascii_lowercase
     
    s3=string.digits
     
    s4=string.punctuation
    
    plen=int(input("Enter password length\n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
     
    print("Your password is: ")
     
    print("".join(random.sample(s,plen)))












