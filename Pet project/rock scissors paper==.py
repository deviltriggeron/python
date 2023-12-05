import random

def game():
    while True:
        spisok = ['rock', 'scissors', 'paper']
        ais = str(random.choice(spisok))
        sp = input('select: "rock = 1", "scissors = 2", "paper = 3"\n')
        if sp == "1":
            print("You select rock, i'm select " + ais)
            if ais == "rock":
                print("draw!\ntry again? or write 'N' to leave")
            elif ais == "scissors":
                print("you win!\nselect again or write 'N' to leave")
            elif ais == "paper":
                print("you lose!\ntry again? or if you are scared then write 'N'")
        elif sp == "2":
            print("You select scissors, i'm select " + ais)
            if ais == "rock":
                print("you lose!\ntry again? or if you are scared then write 'N'")
            elif ais == "scissors":
                print("draw!\ntry again? or write 'N' to leave")
            elif ais == "paper":
                print("you win!\nselect again or write 'N' to leave")
        elif sp == "3":
            print("You select paper, i'm select " + ais)
            if ais == "rock":
                print("you win!\nselect again or write 'N' to leave")
            elif ais == "scissors":
                print("you lose!\ntry again? or if you are scared then write 'N'")
            elif ais == "paper":
                print("draw!\ntry again? or write 'N' to leave")
        elif sp == "N":
            print('bye')
            exit(game)
        elif sp == "n":
            print('bye')
            exit(game)
        else:
            print('select number')


game()
