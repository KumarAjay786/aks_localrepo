import random
def gamewon(compu,you):
 if compu==you:
        return None
 elif compu=='s':
        if you=='w':
            return False 
        elif you=='g':
            return True 
 elif compu=='w':        
        if you=='g':
         return False
        elif you=='s':
            return True
 elif compu=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("Computer turn Snake(s),Water(w),Gun(g):?\n")
randNo=random.randint(1,3)
compu=(randNo)
if randNo==1:
 compu =='s'
elif randNo==2:
    compu=='w'
elif randNo==3:      
    compu=='g'
you=input("your turn Snake(s),Water(w),Gun(g):?\n")
a=gamewon(compu ,you)
print(f"computer choose:\t{compu}")
print(f"you choose:\t{you}")
if a==None:
    print("its a tie")
elif a:
    print("You won!!!")    
else:
    print("you looose")
    # hfhgf