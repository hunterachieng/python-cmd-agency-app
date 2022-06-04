# from argparse import _NArgsStr
import click
import csv
from sorting import MergeSort
from searching import SearchCSV

@click.group()
def main():
    """ Reads CSVs, sorts, and writes into them """
    
    pass

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
        print (f"Couldn't write into file at {file_name}. Error: {e}")

@click.command(name='sorting')
@click.argument('file_name', type=click.Path(exists=True))
def csv_read_and_sort(file_name):
    return csv_read_details(file_name)



# searching through the csv

def search_csv (file_name, target, finder):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
      
        things = SearchCSV(data,target, finder)
        print(things.search())


@click.command(name='searching')
@click.argument('file_name', type=click.Path(exists=True), nargs = 1)
@click.argument('target', nargs = 1)
@click.argument('finder',nargs = 1)
def csv_search(file_name, target, finder):
    return search_csv(file_name, target, finder)



    
main.add_command(csv_read_and_sort,'sorting')
main.add_command(csv_search,'searching')

if __name__ == "__main__":
    main()