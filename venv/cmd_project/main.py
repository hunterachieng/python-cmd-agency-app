import csv
from sorting import MergeSort
from searching import SearchCSV

import pdb
def search_csv (file_name,  finder):
    # with open(file_name, "r") as file:
    #     reader = csv.DictReader(file)
    #     data = list(reader)
    #     print(data)
      
        # things = SearchCSV(data,target, finder)
        # print(things.search())
    num = [1,2,3,4,5,6,7,8]
    left = 0
    right = len(num) -1
    target = 7
    while left < right:
        mid = (left+right) //2
        if num[mid] == target:
            return num[mid]
        else:
            if num[mid] < target:
                left = mid +1 
            if num[mid] > target:
                right = mid-1

   
print(search_csv("real-estate-sample.csv", 'providerListingId'))

