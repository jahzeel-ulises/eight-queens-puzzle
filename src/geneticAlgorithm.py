import random
import time

class AlgoritmoGenetico():
    def __init__(self, len_objetivo:int, vocabulario:list,func_actitud) -> None:
        """AlgoritmoGenetico´s constructor.

        Args:
            self: Self@AlgoritmoGenetico,
            len_objetivo: int,
            vocabulario: list,
            func_actitud: Any
        
        Returns:
            None
        """
        #Hiperparameters
        self.vocabulario = vocabulario
        self.longitud_objetivo = len_objetivo
        self.calcular_aptitud = func_actitud

        #Threading
        self.finalize = False

    def __generar_individuo(self, longitud:int)->list:
        """Generates an individual of the population

        Args:
            self: Self@AlgoritmoGenetico,
            longitud: int
        Returns:
            list
        """
        return [random.choice(self.vocabulario) for _ in range(longitud)]

    def __seleccion_ruleta(self, poblacion:list)->list:
        """Selects an individual of the population ramdomly, biased by the fitness.

        Args:
            self: Self@AlgoritmoGenetico,
            poblacion: list
        Returns:
            list 
        """
        aptitudes = [self.calcular_aptitud(individuo) for individuo in poblacion]
        total_aptitudes = sum(aptitudes)
        probabilidad_seleccion = [i/total_aptitudes for i in aptitudes]
        indice_seleccionado = random.choices(poblacion, weights=probabilidad_seleccion)
        return indice_seleccionado[0]

    def __seleccion_torneo(self,poblacion:list)->list:
        """Selects three individuals of the population randomly and returns who has the greater fitness.
        
        Args:
            self: Self@AlgoritmoGenetico,
            poblacion: Any
        Returns:
            list
        """
        torneo = random.sample(poblacion, 3)
        torneo.sort(key=lambda individuo: self.calcular_aptitud(individuo),reverse=True)
        return torneo[0]


    def __crossover_un_punto(self, padre1, padre2):
        """Combine two individuals using just one crossover point.

        Args:
            padre1: list
            padre2: list
        Retuns:
            list
        """
        punto_corte = random.randint(0, len(padre1) - 1)
        hijo = padre1[:punto_corte] + padre2[punto_corte:]
        return hijo

    def __crossover_dos_puntos(self,padre1, padre2)->list:
        """Combine two individuals using two crossover points.

        Args:
            padre1: list
            padre2: list
        Retuns:
            list
        """
        punto_corte1, punto_corte2 = sorted(random.sample(range(len(padre1)), 2))
        hijo = padre1[:punto_corte1] + padre2[punto_corte1:punto_corte2] +padre1[punto_corte2:]
        return hijo

    def __mutacion(self, individuo)->list:
        """Mutates one individual, changing one element of the list randomly.

        Args:
            self: Self@AlgoritmoGenetico,
            individuo: Any
        Returns:
            list
        """
        indice_mutacion = random.randint(0, len(individuo) - 1)
        nuevo_caracter = random.choice(self.vocabulario)
        individuo_mutado = individuo.copy()
        individuo_mutado[indice_mutacion] = nuevo_caracter
        return individuo_mutado

    def algoritmo_genetico(self, tamano_poblacion:int = 100, generaciones:int = 1000, prob_mutacion:float = 0.2,selection:int = 0, crossover:int=0)->list:
        """Execute the genetic algorithm to maximaze the fitness function of the object.

        Args:
            self: Self@AlgoritmoGenetico,
            tamano_poblacion: int = 100,
            generaciones: int = 1000,
            prob_crossover: float = 0.8,
            prob_mutacion: float = 0.2
            selection: int = 0
        Returns:
            list
        """

        poblacion = [self.__generar_individuo(self.longitud_objetivo) for _ in range(tamano_poblacion)]

        for _ in range(generaciones):
            poblacion = sorted(poblacion, key=lambda individuo: self.calcular_aptitud(individuo), reverse=True)
            self.mejor_individuo = poblacion[0]

            nueva_poblacion = []

            while len(nueva_poblacion) < tamano_poblacion:
                if selection:
                    padre1 = self.__seleccion_ruleta(poblacion)
                    padre2 = self.__seleccion_ruleta(poblacion)
                else:
                    padre1 = self.__seleccion_torneo(poblacion)
                    padre2 = self.__seleccion_torneo(poblacion)

                if crossover:
                    hijo = self.__crossover_dos_puntos(padre1, padre2)
                else:
                    hijo = self.__crossover_un_punto(padre1, padre2)

                if random.random() < prob_mutacion:
                    hijo = self.__mutacion(hijo)

                nueva_poblacion.append(hijo)
    
            poblacion = nueva_poblacion

            if self.finalize:
                return
            
            time.sleep(100/1000)

        mejor_individuo = poblacion[0]
        return mejor_individuo