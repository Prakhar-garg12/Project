'''
                   Task 4
Rock-Paper-Scissors Game

 
'''
import random
print("1 for Rock\n 2 for Paper \n 3 for Scissor")
user=int(input("Enter your choice: "))
 
comp=random.randint(1,3)
print(f"User = {user}")
print(f"Computer = {comp}")
if user==comp:
     print("Both are same ! It's tie!")
elif user==1:
     if comp==2:
          print("Paper covers rock ! , Computer Win!")
     elif comp==3:
          print("Rock smashes scissor! User wins!")
elif user == 2:
    if comp == 1:
        print("Paper covers rock! User wins!")
    elif comp == 3:
        print("Scissor cuts paper! Computer wins!")
elif user == 3:
    if comp == 1:
        print("Rock smashes scissor! Computer wins!")
    elif comp == 2:
        print("Scissor cuts paper! User wins!")


      













