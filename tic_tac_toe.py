import random

# Initialize board
board = [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def empty_spaces(board):
    return ' ' in board

def winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

def minimax(board, depth, is_maximizing):
    if winner(board, 'O'):
        return 1
    elif winner(board, 'X'):
        return -1
    elif not empty_spaces(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

def player_move(board):
    move = None
    while move not in available_moves(board):
        move = int(input("Enter your move (1-9): ")) - 1
        if move not in available_moves(board):
            print("Invalid move. Try again.")
    return move

def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while empty_spaces(board) and not winner(board, 'X') and not winner(board, 'O'):
        # Human move
        move = player_move(board)
        board[move] = 'X'
        print_board(board)

        if winner(board, 'X'):
            print("You win!")
            break
        elif not empty_spaces(board):
            print("It's a tie!")
            break

        # AI move
        move = best_move(board)
        board[move] = 'O'
        print("AI plays:")
        print_board(board)

        if winner(board, 'O'):
            print("AI wins!")
            break
        elif not empty_spaces(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
