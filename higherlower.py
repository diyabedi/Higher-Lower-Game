# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:32:37 2024

@author: diyab
"""
#Display ART
from art_highlow import logo, VS
from datafile import data
import random
"""Format the account data """
def format(account):
    account_name=account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"

# - Use if statement to check if user is correct
def check_answer(user_guess, a_follow, b_follow):
    if a_follow>b_follow:
        return user_guess=="a"
    else:
        return user_guess=="b"
 
print(logo)
count =0
gameplay=True
account_b = random.choice(data)

while gameplay:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
        
    print(f"Compare A: {format(account_a)}")
    print(VS)
    print(f"Against B: {format(account_b)}")
        
    #ASK user for a guess 
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" *20)
    print(logo)


    #Check answer if user is correct 
    # - Get followers of each account
    follower_a = account_a["follower_count"]
    follower_b= account_b["follower_count"]
    is_correct=check_answer(guess, follower_a, follower_b)

    #Giver user feedback and Increase the score or psst lost
    if is_correct:
        count+=1
        print(f"You're right! Current Score: {count}")
    else:
        print(f"Sorry, that's wrong. Final Score: {count}")
        gameplay=False

    









        
        