def solution(board):
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col-1,0),min(col+2,len(board))):
                    for i in range(max(row-1,0),min(row+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)

    return answer
