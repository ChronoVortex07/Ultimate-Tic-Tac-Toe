import numpy as np

def check_winning_move(board, current_player):
    # Check rows
    for row in board:
        if np.count_nonzero(row == current_player) == 2 and np.count_nonzero(row == None) == 1:
            return True

    # Check columns
    for col in board.T:
        if np.count_nonzero(col == current_player) == 2 and np.count_nonzero(col == None) == 1:
            return True

    # Check diagonals
    if np.count_nonzero(np.diag(board) == current_player) == 2 and np.count_nonzero(np.diag(board) == None) == 1:
        return True
    elif np.count_nonzero(np.diag(np.fliplr(board)) == current_player) == 2 and np.count_nonzero(np.diag(np.fliplr(board)) == None) == 1:
        return True

    return False

# Example usage
tic_tac_toe_board = np.array([
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', None, 'O']
])

current_player = 'O'  # Replace with the actual current player ('X' or 'O')

if check_winning_move(tic_tac_toe_board, current_player):
    print(f"Adding a new '{current_player}' will result in a win!")
else:
    print(f"Adding a new '{current_player}' will not result in a win.")