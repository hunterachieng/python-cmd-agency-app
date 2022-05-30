from tokenize import group
import click
import csv
from sorting import MergeSort
def csv_read_details(file_name):
    data = []
    with open(file_name, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    data.append(row)
    sorted = MergeSort(data)
    sorted.sortData()
                    

    # writing to csv
    try:
        print("Writing file...")
        with open(file_name, 'w') as csvfile:
            data_writer = csv.writer(csvfile)
            data_writer.writerow(header)
            data_writer.writerows(data)
        print(f"File created : {file_name}")
    except IOError as e:
        print(f"Couldn't write into file at {file_name}. Error: {e}")

# csv_read_details("real-estate-sample.csv", "r")

@click.command()
@click.argument('file_name', type=click.Path(exists=True))
def main(file_name):
    """ Reads CSVs, sorts, and writes into them """
    
    csv_read_details(file_name)
    


if __name__ == "__main__":
    main()