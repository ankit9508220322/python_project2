import random
item_list = ["gun","paper","scissor"]
user_choice = input("enter the move = gun , paper , scissor:= ")
computer_choice= random.choice(item_list)

print(f"user choice  = {user_choice},computer choice=: {computer_choice}")

if user_choice == computer_choice:
    print("both chooses same : = match tie");

elif user_choice == "gun":
    if computer_choice == "paper":
        print("paper cover gun = computer: ")
    else:
        print("gun sameshes scissor = you win  ")

elif user_choice == "paper":
    if computer_choice == "scissor":
        print("scissor cut paper, computer win")
    else:
        print("paper covers gun , you will")

elif user_choice == "scissor":
    if computer_choice == "paper":
        print("scissor cut paper, you win")
    else:
        print("gun smashes scissor , computer win ");
            