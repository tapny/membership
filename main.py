import eventbrite_client as eb
import mailchimp_client as mc

START_YEAR = 2014    # The year to pull events for
LIST_ID = '8196fa6dba'    # The MailChimp ID for TEST List

def formatSubscribers(subscribers):
    """
    This function formats the subscribers in the correct structure
    for the MailChimp API
    """
    output = []
    for subscriber in subscribers:
        output.append( \
            {
                "email": {"email": subscriber[2]}
                , "merge_vars": {
                    "FNAME": subscriber[0]
                    , "LNAME": subscriber[1]
                }
            }
        )
    return output

if __name__ == "__main__":
    subscribers = []
    
    # Get all new subscribers from the events this year
    events = eb.get_events_for_year(START_YEAR)
    for event in events:
        try:
            subscribers = subscribers + eb.get_new_subscribers(event)
        except:
            continue

    # Remove duplicates
    # This doesn't seem to be working correctly but MailChimp removes duplicates for you
    subscribers = list(set(subscribers))

    # Add subscribers and print the result
    result = mc.addSubscribers(LIST_ID, formatSubscribers(subscribers))
    print result
