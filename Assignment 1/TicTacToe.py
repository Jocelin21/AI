# Display Tic-Tac-Toe board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def display(board):
    for row in board:
        print('|'.join(row))

# Check if the current player has won
def win(board, player):
    # Row
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Column
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonal
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Check if the board is full (a tie)
def tie(board):
    return all(cell != ' ' for row in board for cell in row)

# Computer's move using minimax
def compMove(board):
    def minimax(board, depth, isMaximizing):
        scores = {'X': 1, 'O': -1, 'Tie': 0}

        if win(board, 'X'):
            return scores['X']
        if win(board, 'O'):
            return scores['O']
        if tie(board):
            return scores['Tie']

        if isMaximizing:
            bestScore = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        bestScore = min(score, bestScore)
            return bestScore

    bestMove = None
    bestScore = -float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = (i, j)

    return bestMove

while True:
    display(board)
    
    row = int(input("Enter row   : ")) - 1
    col = int(input("Enter column: ")) - 1

    board[row][col] = 'O'
    
    if win(board, 'O'):
        display(board)
        print("You win!")
        break

    if tie(board):
        display(board)
        print("It's a tie!")
        break

    compRow, compCol = compMove(board)
    board[compRow][compCol] = 'X'

    if win(board, 'X'):
        display(board)
        print("You lose!")
        break
