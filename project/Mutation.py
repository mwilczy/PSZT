from random import randint

class Mutation:
    def __init__(self, newPopulation, itemNumber, mutationPercent):
        self.newPopulation = newPopulation
        self.mutationPercent = mutationPercent
        self.itemNumber = itemNumber
        self.resolution = 10000
    def Mutation(self):
        for chrom in self.newPopulation:
            indexes = chrom.calculateIndexes()
            for el in range(0, self.itemNumber):
                if randint(1, self.resolution) <= self.mutationPercent * 100:
                    if el in indexes:
                        chrom.removeItemIndex(el)
                    else:
                        chrom.putItemIndex(el)
        return self.newPopulation
