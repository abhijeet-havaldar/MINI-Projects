import random

item_list = ["Rock","Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor =")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper covers Rock = You Win")
    else:
        print("Scissor cuts Paper = Computer Win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor = Computer Win")
    else:
        print("Scissor cuts Paper = You Win")
        