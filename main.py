import csv
from sorting import MergeSort
sorted_data = []
with open('real-estate-sample.csv', 'r') as file:
            reader = csv.reader(file)
            sorted_data.extend(list(reader))
sorted = MergeSort(sorted_data)
print(sorted.sortData())