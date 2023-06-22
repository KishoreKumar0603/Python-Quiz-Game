import random

def get_choices():
    pl_ch=input("Enter a choice (rock,paper,scissor): ")
    cs=["paper","rock","scissor"]
    cm_ch=random.choice(cs)
    choices={"player":pl_ch,"computer":cm_ch}
    return choices

def win(player,computer):
    print(f"You Chose {player}, Computer Chose {computer}")
    if player==computer:
        return "Its a Tie!"
    elif player=="rock":
        if computer=="scissor":
            return "Rock Smashes Scissor! You Win..."
        else:
            return "Paper Covers Rock! You Lose..."
    elif player=="scissor":
        if computer=="rock":
            return "Rock Smashes Scissor! You Lose..."
        else:
            return "Scissor Cuts Paper! You win..."
    elif player=="paper":
        if computer=="rock":
            return "Paper Covers Rock! You Win..."
        else:
            return "Scissor Cuts Paper! You Lose..."
choices=get_choices()
result=win(choices["player"],choices["computer"])
print(result)