import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
torX = initial_tx
torY = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    directionX = ''
    directionY = ''

    if torY > light_y:
        directionY = 'N'
        torY = torY - 1
    elif torY < light_y:
        directionY = 'S'
        torY = torY + 1
    
    if torX > light_x:
        directionX = 'W'
        torX = torX -1
    elif torX < light_x:
        directionX = 'E'
        torX = torX + 1
    
    print(directionY+directionX)
