import csv
from sorting import MergeSort
data = []
with open('real-estate-sample.csv', 'r') as file:
            reader = csv.reader(file)
            data.extend(list(reader))
sorted = MergeSort(data)
print(sorted.sortData())