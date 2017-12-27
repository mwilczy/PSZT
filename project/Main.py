import sys

from project.Population import Population

from project.SelectionAndCrossover import SelectionAndCrossover
from project.Input import Input


class Controller:
    def __init__(self, path=""):
        self.inputController = None
        self.path = path
    def readFromFile(self, path):
        self.inputController = Input(open(path))
    def readFromStdin(self):
        self.inputController = Input(sys.stdin)
    def run(self):
        self.readFromFile(self.path)
        self.inputController.readFromSource()

        #print(self.inputController.populationInfo.bagCapacity)
        #print(self.inputController.populationInfo.objectList)

        self.newPopulation = Population(self.inputController.populationInfo)
        self.newPopulation.generateRandomPopulation()


        testCounter = 0
        while self.newPopulation.checkAllPopulationFitness() and testCounter < 1000:
            # Selection and crossover

            self.newSelection = SelectionAndCrossover(self.newPopulation)

            self.newSelection.SelectPair()

            self.newSelection.Crossover()

            testCounter += 1


             # Mutation and choosing of new population



# temporary just to test it easily
mainController = Controller("C:/Users/john/Desktop/testy.txt")
mainController.run()

#print(mainController.newPopulation.chromosomePopulation)


