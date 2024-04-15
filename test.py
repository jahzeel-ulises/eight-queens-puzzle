import math
import random
from src.geneticAlgorithm import AlgoritmoGenetico
from src.queens import *
vocabulario = [0,1,2,3,4,5,6,7]
AG = AlgoritmoGenetico(8,vocabulario,fitness_function)
mejor = AG.algoritmo_genetico(generaciones=5000)
print(mejor,function_cost(mejor))