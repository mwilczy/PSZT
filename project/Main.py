import sys

from project.Population import Population

from project.Selection import Selection
from project.Crossover import Crossover
from project.Mutation import Mutation
from project.Input import Input


class Controller:
    def __init__(self, path="", mutationPercent = 20, selectionPercent = 0.5):
        self.inputController = None
        self.path = path
        self.mutationPercent = mutationPercent
        self.selectionPercent = selectionPercent
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
        while self.newPopulation.checkAllPopulationFitness() and testCounter < 100000000000:

            (self.selected, self.notSelected) = Selection(self.newPopulation, self.selectionPercent).SelectionIn()

            self.selected = Crossover(self.selected).Crossover()
            
            self.selected = Mutation(self.selected, self.newPopulation.populationInfo.itemNumber, self.mutationPercent).Mutation()

            self.newPopulation = Selection(self.newPopulation).SelectionOut(self.selected, self.notSelected)

            testCounter += 1

            print testCounter




# temporary just to test it easily
mainController = Controller("C:/pszt/testy.txt")
mainController.run()

#print(mainController.newPopulation.chromosomePopulation)


