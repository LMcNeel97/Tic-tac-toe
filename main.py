from helper import draw_board, check_turn, check_winner

# import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
turn = 0

while playing:
    # Reset the screen
    # os.system('cls' if os.name == 'nt' else 'clear')
    if turn == 0:
        print("Player One Start:")
    draw_board(spots)
    if turn >= 9:
        print("Draw!")
        draw_board(spots)
        break

    winner = check_winner(spots)
    if winner:
        print(f"{winner} Wins!")
        draw_board(spots)
        break

    # get Input (stored as choice) from the player
    choice = input()
    if choice == 'q':
        playing = False
        continue

    if choice.isdigit() and 1 <= int(choice) <= 9:
        if spots[int(choice)] not in ['O', 'X']:  # Used to check if a spot has been taken by the other player
            spots[int(choice)] = check_turn(turn)
            turn += 1
        else:
            print("Spot is already taken. Please choose another spot.")
    else:
        print("Invalid input, please select a value between 1 and 9.")
