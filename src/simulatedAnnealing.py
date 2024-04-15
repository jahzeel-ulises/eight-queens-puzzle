import math
import random
import time

class SimulatedAnnealing():
    def __init__(self,func_initial, func_cost, func_createNeighbour, max_iter:int = 1000, temp_ini:int = 1000, func_prob:str = 'exponencial', fe:float = 0.95) -> None:
        """SimulatedAnnealing's class constructor.
        
        Args:
            self: Self@SimulatedAnnealing,
            func_initial: function,
            func_cost: function,
            func_createNeighbour: function,
            max_iter: int = 100,
            temp_ini: int = 1000,
            func_prob: str = 'exponencial',
            fe: float = 0.95
        
        Returns:
            None
        """

        #Set user functions
        self.create_initial_state = func_initial
        self.calculate_cost = func_cost
        self.create_neighbour = func_createNeighbour

        #Set hiperparameters
        self.max_iteraciones = max_iter
        self.temperatura_inicial = temp_ini
        self.opcion = func_prob
        self.factor_enfriamiento = fe

        #Thread
        self.finalize = False
        self.pause = 10

    def set_parameters(self,temp_ini:int=1000,func_prob:str = 'exponencial', fe:float = 0.95, max_iter:int = 1000)->None:
        """Class setter.

        Args:
            self: Self@SimulatedAnnealing,
            temp_ini: int = 1000,
            func_prob: str = 'exponencial',
            fe: float = 0.95,
            max_iter: int = 1000

        Returns:
            None
        """
        #Set hiperparameters
        self.temperatura_inicial = temp_ini
        self.opcion = func_prob
        self.factor_enfriamiento = fe
        self.max_iteraciones = max_iter

    def __temperature_change(self,temperatura_actual:float)->float:
        """Receives a temperature value and returns the new temperature value reduced by the cooling factor.

        Args:
            self: Self@SimulatedAnnealing,
            temperatura_actual: float

        Returns:
            float
        """
        if self.opcion == 'lineal':
            return temperatura_actual*(1-(0.951-self.factor_enfriamiento))
        elif self.opcion == 'exponencial':
            return temperatura_actual * self.factor_enfriamiento

    def simulatedAnnealing(self) -> tuple:
        """Execute the simulated annealing to optimize the cost function of the object.
        Args:
            self: Self@SimulatedAnnealing
        
        Returns:
            tuple[Any,float]
        """
        self.current = self.create_initial_state()

        # Evaluates the intial cost
        current_cost = self.calculate_cost(self.current)
        
        temperatura_actual = self.temperatura_inicial
        
        for _ in range(self.max_iteraciones):
            # Creates an neighbor
            neighbor = self.create_neighbour(self.current)

            # Evaluates neighbor´s cost
            cost_neighbor = self.calculate_cost(neighbor)
            delta_cost = cost_neighbor - current_cost
            if delta_cost < 0:
                self.current = neighbor
                current_cost = cost_neighbor
            else:
                acceptance_prob = math.exp(-delta_cost / temperatura_actual)
                rand_num = random.random()
                if rand_num < acceptance_prob:
                    self.current = neighbor
                    current_cost = cost_neighbor

            temperatura_actual = self.__temperature_change(temperatura_actual)
            time.sleep(self.pause/1000)
            if self.finalize:
                return

        self.cost = current_cost

        return self.current, self.cost