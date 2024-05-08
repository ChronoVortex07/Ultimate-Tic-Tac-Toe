import numpy as np
import time

def check_win(board: list[list[str | None]]) -> str | None:
    board = np.array(board).reshape((3,3))
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != None:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    
    return None

def check_two_board_win(board: list[list[str | None]], current_player: str) -> str | None:
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

def evaluate_state(board: list[list[str | None]], current_player: str, move_coords: tuple[int, int, int, int], verbose = False) -> int:
    # reshape the board into a 3x3x3x3 array
    board = np.array(board).reshape((3,3,3,3))
    
    # check if the move was made on a valid cell
    if board[move_coords[0], move_coords[1], move_coords[2], move_coords[3]] != None:
        raise ValueError('Invalid move')
    
    score = 0
    
    # get the sub-board that the move was made on
    old_sub_board = board[move_coords[0], move_coords[1]]
    new_sub_board = old_sub_board.copy()
    new_sub_board[move_coords[2], move_coords[3]] = current_player
    
    # get the state of the main board after the move
    new_main_board = np.empty((3,3), dtype = object)
    board[move_coords[0], move_coords[1], move_coords[2], move_coords[3]] = current_player
    for row in range(3):
        for col in range(3):
            new_main_board[row, col] = check_win(board[row, col])
    new_main_board = np.array(new_main_board)
    
    # winning a small board gives 5 points
    if check_win(new_sub_board) == current_player:
        if verbose:
            print('won a sub-board, score +5')
        score += 5
        
        # if the win was on the corner sub-boards, give an additional 3 points
        if move_coords[0] in [0, 2] and move_coords[1] in [0, 2]:
            if verbose:
                print('won a corner sub-board, score +3')
            score += 3
            
        # if the win was on the center sub-board, give an additional 10 points
        if move_coords[0] == 1 and move_coords[1] == 1:
            if verbose:
                print('won the center sub-board, score +10')
            score += 10
            
    # getting any square in the center sub-board gives 3 point
    if move_coords[0] == 1 and move_coords[1] == 1:
        if verbose:
            print('got a square in the center sub-board, score +3')
        score += 3
    # getting the center square of a sub-board gives 3 points
    elif move_coords[2] == 1 and move_coords[3] == 1:
        if verbose:
            print('got the center square of a sub-board, score +3')
        score += 3
        
    # two board wins where the third board is not won gives 4 points
    if check_two_board_win(new_main_board, current_player):
        if verbose:
            print('two board win in main board, score +4')
        score += 4
    
    # if this happens in the sub-board, gives 2 points
    if check_two_board_win(new_sub_board, current_player):
        if verbose:
            print('two board win in sub-board, score +2')
        score += 2
        
    # if your move results in the opponent moving to a sub-board that is won, deduct 2 points
    if check_win(board[move_coords[2], move_coords[3]]) == current_player:
        if verbose:
            print('opponent got a free move, score -2')
        score -= 2
        
    # if the main board is won, give 100 points
    if check_win(new_main_board) == current_player:
        if verbose:
            print('won the main board, score +100')
        score += 100
    
    return score
            
start_time = time.time()
print(evaluate_state(
    [
        [None, None, None, None, None, None, None, 'X', 'X'], 
        [None, None, None, None, 'O', None, 'X', 'X', 'X'], 
        [None, None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None, 'X'], 
        ['O', 'O', None, None, 'X', None, None, 'X', None], 
        [None, None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None, None], 
        ['O', 'X', None, 'O', 'X', None, None, None, None], 
        [None, 'O', None, None, 'O', None, None, 'O', None]
    ], 
    'X', 
    # (0, 0, 2, 0)
    (2, 1, 2, 1),
    verbose = True
))
print(time.time() - start_time)