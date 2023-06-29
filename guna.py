import random
n=input("Enter your name?")
print("hi {},lets start the game!!!".format(n))
chances=6
c=1
t=True
while t==True:
    number=str(random.randint(101,999))
    if number[0]==number[1] or number[1]==number[2] or number[2]==number[0]:
        t=True
    else:
        t=False
#print("enter a number to start the game!")
while chances>0:
    cows=0
    bulls=0
    check=input("enter number")
    for i in range(len(check)):
        
        if check[i]==number[i]:
            bulls=bulls+1
        elif check[i] in number:
            cows=cows+1
    chances=chances-1
    if bulls==3:
        print("congrats!!!,You won the Game")
        c=0  
        break
    else: 
        print(bulls,"bulls and ",cows,"cows.",chances,"chances left!")
         
if c!=0:
    print("You lost the game ",number," is the requried input") 
    
            
                
     



