import csv
from abc import ABC, abstractmethod

class CSVSort(ABC):

    @abstractmethod
    def sortData(self):
        pass


    # @abstractmethod
    # def search(self):
    #     pass




class MergeSort(CSVSort):
   
    
    def  __init__(self, data):
        self.data = data
    
    def sortData(self):
        if len(self.data) >1:
            middle = len(self.data)//2
            left =  self.data[1:middle]
            right = self.data[middle:]

            leftSort = MergeSort(left)
            leftSort.sortData()

            rigthSort = MergeSort(right)
            rigthSort.sortData()

           
            

            i = j=k=0
            while i < len(left) and j < len(right):
                if left[i][1] < right[j][1]:
                    self.data[k] = left[i]
                    i +=1
                
                else:
                    self.data[k]=right[j]
                    j+=1
                k+=1
            
            while i < len(left):
                self.data[k] = left[i]
                i+=1
                k+=1
            
            while j < len(right):
                self.data[k] = right[j]
                j+=1
                k+=1
        
        print(self.data)
    


data = []
with open('real-estate-sample.csv', 'r') as file:
            reader = csv.reader(file)
            data.extend(list(reader))
            # print(data)
sorted = MergeSort(data)
print(sorted.sortData())

   
