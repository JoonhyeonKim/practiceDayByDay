def solution(keyinput, board):
    answer = []
    xMax = int(board[0])/2
    xMin = -xMax
    yMax = int(board[1])/2
    yMin = -yMax
    xCoord = 0
    yCoord = 0
    
    print(xMax, xMin, yMax, yMin)
    
    for command in keyinput:
        if command == 'up' and yCoord <= yMax-1: ## -1 for step size, it should be checked before the step is activated
            yCoord += 1
        elif command == 'down' and yCoord >= yMin+1: ## +1 for step size, the reasoning is same as above
            yCoord -= 1
        elif command == 'right' and xCoord <= xMax-1:
            xCoord += 1
        elif command == 'left' and xCoord >= xMin+1:
            xCoord -= 1
        else:
            yCoord = yCoord
            xCoord = xCoord
    
    answer.append(xCoord)
    answer.append(yCoord)
    
    return answer
  
  ## another solution
  
  def is_over_board(value, max_value):
    if value < -max_value:
        return True
    elif value > max_value:
        return True
    return False


def solution(keyinput, board):
    key_results = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    max_width, max_height = board[0] // 2, board[1] // 2

    loc = [0, 0]
    for key in keyinput:
        new_loc = [loc[0] + key_results[key][0], loc[1] + key_results[key][1]]

        if is_over_board(new_loc[0], max_width):
            continue
        if is_over_board(new_loc[1], max_height):
            continue
        loc = new_loc
    return loc
