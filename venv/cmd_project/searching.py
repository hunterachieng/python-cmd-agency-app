from abstract import CSVSearch

class SearchCSV(CSVSearch):
    def __init__(self,data, target, finder ):
        self.data = data
        self.target =target
        self.finder = finder
    
    def search(self):
        left = 0
        right = len(self.data)-1
       
        while left <= right:
            mid = (left +right) //2
            if self.target == self.data[mid][self.finder]:
                return self.data[mid]
            else:
                if self.target < self.data[mid][self.finder]:
                   right = mid -1 
                if self.target > self.data[mid][self.finder]:              
                    left = mid +1
    
    
        
        

                


        
        