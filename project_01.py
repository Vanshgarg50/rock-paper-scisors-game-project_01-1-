def rps(you,comp):
   if you==comp:
    return 0
   if you=='r' and comp=='s':
    return 1
   if you=='s' and comp=='p':
    return 1  
   if you=='p' and comp=='r':
    return 1  
   if you=='s' and comp=='r':
    return -1    
   if you=='p' and comp=='s':
    return -1   
   if you=='r' and comp=='p':
    return -1   


import random

n=random.randint(1,3)

if n==1:
      comp='r'
elif n==2:
      comp='p'
elif n==3:
      comp='s'  


you=input("enter r for rock, p for paper, s for scisors\n")


result = rps(you,comp)
print(f"you choose {you} and comp chooses {comp}")
if result==1:
    print("you win")
elif result==0:
    print("draw")
else:
    print("you lose")

    

