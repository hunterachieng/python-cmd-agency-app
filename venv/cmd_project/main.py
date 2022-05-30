import csv
from sorting import MergeSort


def csv_read_details(file_name, mode):
    data = []
    with open(file_name, mode) as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    data.append(row)
    sorted = MergeSort(data)
    sorted.sortData()

    # writing to csv
    with open(file_name, 'w') as csvfile:
        data_writer = csv.writer(csvfile)
        data_writer.writerow(header)
        data_writer.writerows(data)

csv_read_details("real-estate-sample.csv", "r")