while 1:
    print('''menu:
    1.Play new game
    2.exit''')
    c=int(input("\n>"))
    if c==1:
        b=4
        while not b==1:
            print("\nYou have only 3 chances to win the game: ")
            a=int(input("\nEnter a no: "))
            if a == 3:
                print("\nYou have win (^o^)")
                exit()
            else:
                print("\nWrong no...")

            b -= 1
        print("\nYou have lose!!!!!!")
    elif c==2:
        exit()
    else :
        print("\nEnter valid choice")