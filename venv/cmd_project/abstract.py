from abc import ABC, abstractmethod

class CSVSort(ABC):

    @abstractmethod
    def sortData(self):
        pass

 

class CSVSearch(ABC):
    @abstractmethod
    def search(self):
        pass

class CSVDuplicates(ABC):
    @abstractmethod
    def removeDuplicates(self):
        pass