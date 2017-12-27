from project.Glob import PopulationInfo

class Input:
    def __init__(self, source):
        self.ignoredLines = []
        self.lineCounter = 0
        self._source = source
        self.populationInfo = PopulationInfo()

    def __clean(self):
        self.populationInfo.clean()
        self.ignoredLines = []
        self.lineCounter = 0

    def __readFromIOWrapper(self):
        readLine = self._source.readline()
        readLine = readLine.replace('\n', '')
        return readLine

    def __readCapacity(self):
        self.populationInfo.setBagCapacity(int(self.__readFromIOWrapper()))
        self.lineCounter += 1

    def __readItemList(self):
        while (True):
            readLine = self.__readFromIOWrapper()
            if (readLine == ''):
                return
            self.lineCounter += 1
            foundSpace = readLine.find(" ")
            self.__readSingleItemProperties(readLine, foundSpace)

    def __readSingleItemProperties(self, readLine, foundSpace):
        if (foundSpace != -1):
            try:
                objectCapacity = int(readLine[:foundSpace])
                objectValue = int(readLine[foundSpace + 1:])
                self.populationInfo.addNewItem(objectCapacity, objectValue)
            except ValueError:
                print("Bad input line number: " + str(self.lineCounter))
                self.ignoredLines.append(self.lineCounter)

    def result(self):
        return self.populationInfo

    def readFromSource(self):
        self.__clean()
        self.__readCapacity()
        self.__readItemList()