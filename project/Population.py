import random

from project.Chromosome import Chromosome

from project.Glob import fitnessFunction


class Population:
    def __init__(self, populationInfo):
        self.populationInfo = populationInfo
        self.chromosomePopulation = []

    def generateRandomPopulation(self):
        for i in range(self.populationInfo.itemNumber * 10):
            self.chromosomePopulation.append(self.generateOneChromosome())



    def checkAllPopulationFitness(self):
        repeatCount = {}
        totalCount = 0
        for singleChromosome in self.chromosomePopulation:
            chromosomeFitness = fitnessFunction(singleChromosome.calculateIndexes(), self.populationInfo)
            if singleChromosome in repeatCount:
                repeatCount[chromosomeFitness] += 1
            else:
                repeatCount[chromosomeFitness] = 0
            totalCount += 1

        for fitness, count in repeatCount.items():
            if count/totalCount > 0.9:
                return False

        return True

    def generateOneChromosome(self):
        tempIndexes = []
        while True:
            index = random.randrange(0, self.populationInfo.itemNumber)
            if index not in tempIndexes:
                if fitnessFunction(tempIndexes + [index], self.populationInfo) == -1:
                    break
                tempIndexes.append(index)
        print(tempIndexes)
        return Chromosome(tempIndexes, self.populationInfo.itemNumber)
