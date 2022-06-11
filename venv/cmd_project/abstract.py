from abc import ABC, abstractmethod

class CSVSort(ABC):

    @abstractmethod
    def sortData(self):
        pass


   

class CSVSearch(ABC):
    @abstractmethod
    def search(self):
        pass

