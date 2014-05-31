import csv
from eventbrite_client import get_new_subscribers

START_YEAR = 2014

def write_to_csv(filename, writelist):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)

if __name__ == "__main__":
    pass
    
