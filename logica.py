import random
import pygame
import numpy as np

pygame.init()

GameState = True

black = ( 0, 0, 0)

pos = 0

# screenw = 600
# screenh = 750
# # screen = pygame.display.set_mode((screenw,screenh))

tablero = ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

preg = (['1', '2', '3', '4', '5', '6', '7', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

dado = 0

tablero[pos] = 1

    # dado = random.randint(1, 6)

    # for i in range(len(tablero)):
    #     if tablero[i] == 1:
    #         print("preg")
    #         print(preg[i+1])
  
    # tablero[pos] = 0
    # tablero[pos+dado] = 1
    # pos += dado
    
x = 0

while x != 30 or pos >= 36:
    print("presione enter para lanzar dado")
    input()
    dado = random.randint(1, 6)
    print("dado", dado)

    tablero[pos] = 0
    pos += dado
    tablero[pos] = 1

    print(tablero)

    for i in range(len(tablero)):
        if tablero[i] == 1:
            print("preg")
            print(preg[i+1])   
        
    x += 1
