
class PopulationInfo:
    def __init__(self):
        self.bagCapacity = 0
        self.objectList = []
        self.itemNumber = 0
    def clean(self):
        self.__init__()
    def addNewItem(self, volume, value):
        self.objectList.append([volume, value])
        self.itemNumber += 1
    def setBagCapacity(self, bagCapacity):
        self.bagCapacity = bagCapacity
    def setItemNumber(self):
        self.itemNumber = len(self.objectList)



def fitnessFunction(indexes, populationInfo):
    value = 0
    volume = 0
    for i in indexes:
        volume += populationInfo.objectList[i][0]
        if volume > populationInfo.bagCapacity:
            return -1
        value += populationInfo.objectList[i][1]
    return value
