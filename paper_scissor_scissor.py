import random
print("Winning Rules of the Rock paper scissor game as follows: \n" + "Rock vs paper -> paper win \n" + "Rock vs "
                                                                                                       "scissor -> "
                                                                                                       "Rock win \n"
      + "paper vs scissor -> scissor win \n")
while True:
    print("Enter choice\n 1.Rock \n 2.paper\n 3.scissor\n")
    choice = int(input("User turn :"))
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input :"))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    print("User choice is : " + choice_name)
    print("Computer turns........")
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
    print("computer choice is : " + comp_choice_name)
    print(choice_name + " vs " + comp_choice_name)

    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper win ")
        result = "paper"
    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("paper win ")
        result = "Rock"
    else:
        print("scissor win ")
        result = "scissor"
    if result == choice_name:
        print("User win the game")
    else:
        print("Computer win the game")
    print("Do you want to play again ? (Y/N)")
    answer = input()
    if answer == 'n' or answer == 'N':
        break

print("thanks for playing ")
