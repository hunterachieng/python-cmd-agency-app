import csv
from sorting import MergeSort
from searching import SearchCSV

import pdb
def search_csv (file_name, target, finder):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
      
        things = SearchCSV(data,target, finder)
        print(things.search())
     
   
search_csv("real-estate-sample.csv", 'NULL', 'providerListingId')

