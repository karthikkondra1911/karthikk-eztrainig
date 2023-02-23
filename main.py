import random 
user_score=comp_score=0
arr=["rock","paper","scissor"]
c_choice=random.randint(0,2)
c_choice= arr[c_choice]
for i in range(5):
    
    
    u_choice = input("Enter choice:").lower()
    if u_choice not in arr:
        print("Invalid input")
        comp_score += 1
    if c_choice=="rock" and u_choice=="scissor":
        print("comp won")
        comp_score += 1
    elif c_choice=="paper" and u_choice=="rock":
        print("comp won")
        comp_score += 1
    elif c_choice=="scissor" and u_choice=="paper":
        print("comp won")
        comp_score += 1
    elif c_choice==u_choice:
        print("Draw match")
    else:
        print("user won")
        user_score +=1
    print( {comp_score},{user_score})
    if(user_score>>comp_score):
        print("user won")
    else:
        print("computer won")
    



