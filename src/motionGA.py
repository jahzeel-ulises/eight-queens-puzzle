import threading
from src.geneticAlgorithm import AlgoritmoGenetico
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

def motionGA(tamano_poblacion: int = 100,generaciones: int = 1000,prob_mutacion: float = 0.2,selection: int = 0,crossover: int = 0):
    """Displays the animation of the algorithm."""
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Simulador')
    img = pygame.image.load("src\img.png")
    img = pygame.transform.scale(img,(75,75))
    buscador = AlgoritmoGenetico(8,[0,1,2,3,4,5,6,7],fitness_function)
    x = threading.Thread(target=buscador.algoritmo_genetico,args=[tamano_poblacion,generaciones,prob_mutacion,selection,crossover])
    x.start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                buscador.finalize = True
                return
        screen.fill((255,255,255))
        drawGrid(screen)
        drawQueens(screen,buscador.mejor_individuo,img)
        pygame.display.flip()
