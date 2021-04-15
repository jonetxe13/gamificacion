import random
import pygame

pygame.init()

black = ( 0, 0, 0)

#cambia esta variable para cambiar la posicion de inicio
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
    if pos >= 36:
        pos = 36
        tablero[pos] = 1
        print("enhorabuena, has ganado!! Puedes pedir tu punto extra de la evaluacion a Monica")

    tablero[pos] = 1
    print(tablero)

    for i in range(len(tablero)):
        if tablero[i] == 1:
            print("preg:", preg[i+1])
        
    x += 1