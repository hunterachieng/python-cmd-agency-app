import csv
from sorting import MergeSort
from searching import SearchCSV

import pdb
def search_csv (file_name, target, finder):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        things = SearchCSV(data,target, finder)
        things.search()
        print(things)
    pdb.set_trace()
search_csv("real-estate-sample.csv", '10000890', 'id')

