from abc import ABC, abstractmethod

class CSVSort(ABC):

    @abstractmethod
    def sortData(self):
        pass


   

class CSVSearch(ABC):
    @abstractmethod
    def search(self):
        pass


class CSVPrice(ABC):
    @abstractmethod
    def csvPrice(self):
        pass