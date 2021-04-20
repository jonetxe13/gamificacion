import random
import pygame

pygame.init()

black = ( 0, 0, 0)
white = ( 255, 255, 255)
blue = ( 0, 0, 255)

#cambia esta variable para cambiar la posicion de inicio
pos = 0

screenw = 600
screenh = 750
screen = pygame.display.set_mode((screenw,screenh))
cellsize = 75

tablero = ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

preg = (['tema: texto', 'S.O.', 'Edit texto', 'redes', 'edit imagen sonido y video', 'Edit hojas CÁLCULO', 'comodin para tema imagen', 'Infografía', 'Mapa conceptual', 'línea del tiempo', 'Captura de pantalla', 'Editar imagen', 'comodin para tema sonido', 'PODCAST PRESENTANDOSE', 'soundtrack (youtube .mp3)', 'Descargar de Ivoox', 'Editor sonido u editor online de extras', 'Descarga de soundsnap', 'comodin para tema video', 'VIDEO (youtube mp3)', 'Screen video & Desktop', 'Screen Brower Tab', 'Webcam recording presentandose', 'Editar video u editor online', 'comodin para tema paginas web', 'Full screen captura', 'Editor webpage / editor online', 'Cuaderno digital', 'HTML webpage', 'Firma en correo', 'has llegado al final!'])

dado = 0

tablero[pos] = 1


#dibujar el tablero y el rectangulo de inicio
def tabla():
    pygame.draw.rect(screen, white, (cellsize, cellsize*6, cellsize, cellsize), 3)

    for x in range(1, 8):
        for y in range(1, 7):
            pygame.draw.line(screen, white, ( x*cellsize, cellsize), ( x*cellsize, cellsize*6))
            pygame.draw.line(screen, white, ( cellsize, y*cellsize), ( cellsize*7, y*cellsize))
            pygame.display.update()

def movficha():
    for i in range(len(tablero)):
        if tablero[i] == 1:
            if i >= 1 and i <= 7:
                screen.fill(black)
                tabla()
                pygame.draw.circle(screen, blue, ((cellsize*i) + (cellsize/2), (cellsize*5 + (cellsize/2))), cellsize/3)
                pygame.display.flip()
            elif i >= 7 and i <= 13:
                screen.fill(black)
                tabla()
                pygame.draw.circle(screen, blue, ((cellsize*(i-6)) + (cellsize/2), (cellsize*4 + (cellsize/2))), cellsize/3)
                pygame.display.flip()
            elif i >= 13 and i <= 19:
                screen.fill(black)
                tabla()
                pygame.draw.circle(screen, blue, ((cellsize*(i-12)) + (cellsize/2), (cellsize*3 + (cellsize/2))), cellsize/3)
                pygame.display.flip()
            elif i >= 19 and i <= 25:
                screen.fill(black)
                tabla()
                pygame.draw.circle(screen, blue, ((cellsize*(i-18)) + (cellsize/2), (cellsize*2 + (cellsize/2))), cellsize/3)
                pygame.display.flip()
            elif i >= 25 and i <= 31:
                screen.fill(black)
                tabla()
                pygame.draw.circle(screen, blue, ((cellsize*(i-24)) + (cellsize/2), (cellsize + (cellsize/2))), cellsize/3)
                pygame.display.flip()
    # if pos >= 1 and pos <= 7:
    #     if tablero[pos] == 1:
    #         screen.fill(black)
    #         tabla()
    #         pygame.draw.circle(screen, blue, ((cellsize*pos) + (cellsize/2), (cellsize*5 + (cellsize/2))), cellsize/3)
            
    # elif pos >= 7 and pos <= 13:
    #     if tablero[pos] == 1:
    #         screen.fill(black)
    #         tabla()
    #         pygame.draw.circle(screen, blue, ((cellsize*(pos-6)) + (cellsize/2), (cellsize*4 + (cellsize/2))), cellsize/3)
            
    # elif pos >= 13 and pos <= 19:
    #     if tablero[pos] == 1:
    #         screen.fill(black)
    #         tabla()
    #         pygame.draw.circle(screen, blue, ((cellsize*(pos-12)) + (cellsize/2), (cellsize*3 + (cellsize/2))), cellsize/3)

    # elif pos >= 19 and pos <= 25:
    #     if tablero[pos] == 1:
    #         screen.fill(black)
    #         tabla()
    #         pygame.draw.circle(screen, blue, ((cellsize*(pos-18)) + (cellsize/2), (cellsize*2 + (cellsize/2))), cellsize/3)

    # elif pos >= 25 and pos <= 31:
    #     if tablero[pos] == 1:
    #         screen.fill(black)
    #         tabla()
    #         pygame.draw.circle(screen, blue, ((cellsize*(pos-24)) + (cellsize/2), (cellsize + (cellsize/2))), cellsize/3)

    # pygame.display.update()

x = 0
clock = pygame.time.Clock()

while x != 30 or pos >= 33:
    clock.tick(10)

    print("presione enter para lanzar dado")
    input()
    dado = random.randint(1, 6)
    print("dado", dado)

    screen.fill(black)
    tabla()

    tablero[pos] = 0
    preg[pos] = ' '
    pos += dado

    if pos >= 33:
        pos = 33
        tablero[pos] = 1
        print("enhorabuena, has ganado!! Puedes pedir tu punto extra de la evaluacion a Monica")

    tablero[pos] = 1
    print(tablero)
    
    if pos == 4:
        for p in range(1, 7):
            if preg[p] == ' ':
                print("elige una pregunta del bloque anterior antes de continuar")

    # movficha()
    if pos >= pos and pos < 7:
        screen.fill(black)
        tabla()
        pygame.draw.circle(screen, blue, ((cellsize*pos) + (cellsize/2), (cellsize*5 + (cellsize/2))), cellsize/3)
        print("hola")
    elif pos >= 7 and pos < 13:
        screen.fill(black)
        tabla()
        pygame.draw.circle(screen, blue, ((cellsize*(pos-6)) + (cellsize/2), (cellsize*4 + (cellsize/2))), cellsize/3)
        print("hola2")
        pygame.display.update()
        pygame.display.flip()
    elif pos >= 13 and pos < 19:
        screen.fill(black)
        tabla()
        pygame.draw.circle(screen, blue, ((cellsize*(pos-12)) + (cellsize/2), (cellsize*3 + (cellsize/2))), cellsize/3)
        print("hola3")
    elif pos >= 19 and pos < 25:
        screen.fill(black)
        tabla()
        pygame.draw.circle(screen, blue, ((cellsize*(pos-18)) + (cellsize/2), (cellsize*2 + (cellsize/2))), cellsize/3)
    elif pos >= 25 and pos < 31:
        screen.fill(black)
        tabla()
        pygame.draw.circle(screen, blue, ((cellsize*(pos-24)) + (cellsize/2), (cellsize + (cellsize/2))), cellsize/3)

    print("preg:", preg[pos]) 
    
    pygame.display.flip()
    x += 1
