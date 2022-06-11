from abstract import CSVDuplicates

class RemoveCSVDuplicates(CSVDuplicates):
    def __init__(self, data, id):
        self.data = data
        self.id = id

    
    def removeDuplicates(self):
        hash_map = {i[self.id] :0 for i in self.data}

        for i in range(len(self.data)):
            if hash_map[self.data[i][self.id]] == 0:
                print(self.data[i])
                hash_map[self.data[i][self.id]] = 1
        
        
        
        
