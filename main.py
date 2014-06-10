import csv
import eventbrite_client as eb

START_YEAR = 2014

def write_to_csv(filename, writelist):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)

if __name__ == "__main__":
    subscribers = []
    events = eb.get_events_for_year(2014)
    for event in events:
        try:
            subscribers = subscribers + eb.get_new_subscribers(event)
        except:
            continue

    subscribers = list(set(subscribers))
    print subscribers
