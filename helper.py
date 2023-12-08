def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)


def check_turn(turn):
    if turn % 2 == 0:
        print("Player Two's Turn:")
        return 'X'
    else:
        print("Player One's Turn:")
        return 'O'


def check_winner(spots):
    win_combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]
    for combo in win_combinations:
        if spots[combo[0]] == spots[combo[1]] == spots[combo[2]]:
            return spots[combo[0]]

    return None  # No Winner yet
