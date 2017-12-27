import unittest

from project.Input import Input


class MockTextIOWrapper:
    _data = ""
    def __init__(self, data):
        self._data = data

    def readline(self):
        foundNewLine = self._data.find('\n')
        if (foundNewLine == -1):
            dataTmp = self._data
            self._data = ""
            return dataTmp
        dataTmp = self._data[:foundNewLine + 1]
        self._data = self._data[foundNewLine + 1:]
        print(dataTmp.split())
        return dataTmp


class TestInputClass(unittest.TestCase):
    def testNormal(self):
        testObject = Input(MockTextIOWrapper("15\n13 5"))
        testObject.readFromSource()
        self.assertTrue(testObject.populationInfo.bagCapacity == 15)
        self.assertTrue(testObject.lineCounter == 2)
        self.assertTrue(testObject.populationInfo.objectList[0][0] == 13)
        self.assertTrue(testObject.populationInfo.objectList[0][1] == 5)
    def testEmpty(self):
        pass

if (__name__ == '__main__'):
    unittest.main()