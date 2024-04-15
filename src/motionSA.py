import threading
from src.simulatedAnnealing import SimulatedAnnealing
from src.queens import *

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

size = (600,600)

def drawGrid(screen:pygame.Surface)->None:
    """Draws the grid in the pygame surface"""
    color = 0
    colors = [(135,99,0),(255,255,255)]
    width = int(size[0]/8)
    height = int(size[1]/8)
    for i in range(0,size[0],width):
        for j in range(0,size[1],height):
            pygame.draw.rect(screen,colors[color%2],[i,j,width,height],0)
            color += 1
        color += 1

def drawQueens(screen:pygame.Surface,currentState:list,img)->None:
    """Blits the queens in the grid."""
    width = int(size[0]/8)
    height = int(size[1]/8)

    for i in range(8):
        screen.blit(img,(currentState[i]*height,i*width))

def motionSA(temp_ini:int = 1000, func_prob:str = 'exponencial', fe:float = 0.95,iteration=10000):
    """Displays the animation of the algorithm."""
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Simulador')
    img = pygame.image.load("src\img.png")
    img = pygame.transform.scale(img,(75,75))
    buscador = SimulatedAnnealing(func_initial=createInitialState,func_cost=function_cost,func_createNeighbour=func_createNeighbour,max_iter=iteration)
    buscador.set_parameters(temp_ini, func_prob, fe)
    x = threading.Thread(target=buscador.simulatedAnnealing)
    x.start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                buscador.finalize = True
                return
        screen.fill((255,255,255))
        drawGrid(screen)
        drawQueens(screen,buscador.current,img)
        pygame.display.flip()
