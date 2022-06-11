import csv
from sorting import MergeSort
from searching import SearchCSV
from duplicate import RemoveCSVDuplicates

import pdb
def search_csv (file_name,  finder):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        
        without = RemoveCSVDuplicates(data,finder)
        print(without.removeDuplicates())
      
 

   
search_csv("real-estate-sample.csv", 'id')

