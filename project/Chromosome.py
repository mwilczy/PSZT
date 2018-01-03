

class Chromosome:
    masks = [128, 64, 32, 16, 8, 4, 2, 1]
    def __init__(self, loadedItemsIndexes, itemNumber):
        self.chromeArray = bytearray(int(itemNumber/8) + 1)
        for i in loadedItemsIndexes:
            if i < 0:
                raise IndexError("Chromosome indexes can't be negative")
            self.putItemIndex(i)


    def putItemIndex(self, index):
        self.chromeArray[int(index/8)] |= (128 >> (index % 8))
		
    def removeItemIndex(self, index):
        self.chromeArray[int(index/8)] &= ~(128 >> (index % 8))

    def calculateIndexes(self):
        calculatedIndexes = []
        counterBig = 0
        for chromeByte in self.chromeArray:
            counterSmall = 0
            for mask in self.masks:
                if mask & chromeByte != 0:
                    calculatedIndexes.append(counterBig * 8 + counterSmall)
                counterSmall += 1
            counterBig += 1
        return calculatedIndexes

