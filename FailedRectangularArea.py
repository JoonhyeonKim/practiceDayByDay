def solution(dots):
    answer = 0
    x_dot = [dot[0] for dot in dots]
    y_dot = [dot[1] for dot in dots]
    answer = (max(x_dot) - min(x_dot)) * (max(y_dot) - min(y_dot)) ## xMax - xMin = x length, yMax - yMin = y length (it is always true)
      
    return answer
