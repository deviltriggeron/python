game = 'rock.scissors.paper'
#try win))
while True:
    rsp = input('choose number "rock = 1" "scissors = 2", "paper = 3"\n')
    if rsp == "1":
        print("you choose rock \ni'm choose paper, you lose \ntry again? or if you are scared then write 'N'")
    if rsp == "2":
        print("you choose scissors \ni'm choose rock, you lose \ntry again? or if you are scared then write 'N' ")
    if rsp == "3":
        print("you choose paper \ni'm choose scissors, you lose \ntry again? or if you are scared then write 'N'")
    if rsp == "N":
        exit(game)
    if rsp == "n":
        exit(game)
    else:
        print("choose again, think\n")

