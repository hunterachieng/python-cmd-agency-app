import csv
from sorting import MergeSort
data = []
with open('real-estate-sample.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                data.append(row)
sorted = MergeSort(data)
sorted.sortData()

# writing to csv
with open("real-estate-sample.csv", 'w') as csvfile:
    data_writer = csv.writer(csvfile)
    data_writer.writerow(header)
    data_writer.writerows(data)