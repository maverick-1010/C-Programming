while 1:
    print('''menu:
    1.Play new game
    2.exit''')
    c=int(input("\n>"))
    if c==1:
        b=4
        print("\nYou have only 3 chances to win the game: ")
        while not b==1:
            
            a=int(input("\nEnter a no: "))
            if a == 3:
                print("\nYou have win (^o^)")
                break
            else:
                print("\nWrong no...")

            b -= 1
        if not a==3:
            print("\nYou have lose!!!!!!")
    elif c==2:
        exit()
    else :
        print("\nEnter valid choice")
