import random

def createInitialState()->list:
    """Creates a random initial state for the 8-queens puzzle. The state it's a vector[0-7] where each queen is in the position (v[i], i) para i = 0-7."""
    return [random.randint(0,7) for _ in range(8)]

def check_collision(currentState:list,x:int,y:int,x_increment:int,y_increment:int)->int:
    """Check if a queen threatens another in one direction."""
    x += x_increment
    y += y_increment

    while (x >= 0 and x <= 7) and (y >=0 and y<=7):
        if currentState[y] == x:
            return 1
        x += x_increment
        y += y_increment
    return 0

def function_cost(currentState:list)->int:
    """Returns the total of colission of all queens."""
    cost = 0
    for i in range(8):
        cost += check_collision(currentState,currentState[i],i,0,1)
        cost += check_collision(currentState,currentState[i],i,0,-1)
        cost += check_collision(currentState,currentState[i],i,1,1)
        cost += check_collision(currentState,currentState[i],i,1,-1)
        cost += check_collision(currentState,currentState[i],i,-1,1)
        cost += check_collision(currentState,currentState[i],i,-1,-1)
    return cost

def func_createNeighbour(currentState:list)->list:
    """Create a neighbour of the current state."""
    newState = currentState.copy()
    newState[random.randint(0,7)] = random.randint(0,7)
    newState[random.randint(0,7)] = random.randint(0,7)
    
    return newState

def fitness_function(currentState:list)->int:
    """Returns the total of colission of all queens."""
    cost = 48
    for i in range(8):
        cost -= check_collision(currentState,currentState[i],i,0,1)
        cost -= check_collision(currentState,currentState[i],i,0,-1)
        cost -= check_collision(currentState,currentState[i],i,1,1)
        cost -= check_collision(currentState,currentState[i],i,1,-1)
        cost -= check_collision(currentState,currentState[i],i,-1,1)
        cost -= check_collision(currentState,currentState[i],i,-1,-1)
    return cost