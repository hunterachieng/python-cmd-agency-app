import csv
from sorting import MergeSort
from searching import SearchCSV
from trees import UpdateCSV

import pdb
def search_csv (file_name,  price):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

        tree = UpdateCSV()
        node = tree.buildTree(data, price)
        print(tree.csvPrice(node))
        print(tree.minPrice(node))
       
      
       
  

   
search_csv("real-estate-sample.csv", 'unformattedPrice')

