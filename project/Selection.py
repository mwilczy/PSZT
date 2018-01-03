from project.Glob import fitnessComparator

class Selection:
    def __init__(self, newPopulation, selectionPercent = 1):
        self.newPopulation = newPopulation
        self.selectionPercent = selectionPercent
    def SelectionIn(self):
        sortedPopulation = sorted(self.newPopulation.chromosomePopulation, cmp=fitnessComparator(self.newPopulation.populationInfo), reverse=True)
        firstElements = int(self.selectionPercent * len(self.newPopulation.chromosomePopulation))
        return (self.newPopulation.chromosomePopulation[0:firstElements], self.newPopulation.chromosomePopulation[firstElements: len(self.newPopulation.chromosomePopulation)])
    def SelectionOut(self, selectedPopulation, notSelectedPopulation):
        self.newPopulation.chromosomePopulation = selectedPopulation + notSelectedPopulation
        return self.newPopulation