import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = input("Computer and Player is in a desert. They are standing infront of each other, their hands are on their belt. They are ready to pick one of three posssible options, between rock, paper and scissors: ")

    print("computer: ",computer)
    print("player: ",player)


    if computer == "rock" and player == "paper":
        print("Player has wrapped his opponents rock with his paper!")

    if computer == "rock" and player == "rock":
        print("You and your opponent took rocks, so you smashed them toghether and nothing happened!")

    if computer == "rock" and player == "scissors":
        print("Opponent shattered your scissors in thousand pieces!")

    if computer == "paper" and player == "paper":
        print("Both paper lists smacked together and nothing happened")

    if computer == "paper" and player == "rock":
        print("Opponents paper wrapped your rock, opponent wins!")

    if computer == "paper" and player == "scissors":
        print("Your scissors mercilessly cut the paper sheet")

    if computer == "scissors" and player == "paper":
        print("Opponents scissors mercilessly cut you sheet of paper")

    if computer == "scissors" and player == "rock":
        print("Your rock shatterd opponents scissors")

    if computer == "scissors" and player == "scissors":
        print("Both of you scissors do nothing when you put them together.")

        play_again = input("Play again (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye for now!")

        