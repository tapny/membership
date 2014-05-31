import os
import eventbrite
from datetime import datetime

EB_APP_KEY = os.environ['EB_APP_KEY']
EB_API_KEY = os.environ['EB_API_KEY']

eb_auth_tokens = {'app_key':  EB_APP_KEY, 'user_key':EB_API_KEY}
eb_client = eventbrite.EventbriteClient(eb_auth_tokens)

organizer_id = 1750740997

#attendees = eb_client.event_list_attendees({"id":11666856883})['attendees']

def get_new_subscribers(event_id):
    # only grab emails for those who said "yes" to subscribing to newsletter
    attendees = eb_client.event_list_attendees({"id":event_id})['attendees']
    subscribers = []
    for each in attendees:
        attendee = each['attendee']
        if attendee['answers'] and attendee['answers'][0]['answer']['answer_text'].lower() == "yes":
            first = attendee['first_name']
            last = attendee['last_name']
            email = attendee['email']
            subscribers.append( (first, last, email) )
    return subscribers


def get_events_for_year(year):
    since_date = datetime(year, 1, 1)
    # search for events during param year
    all_events = eb_client.user_list_events({"only_display":"title, start_date, id"})['events']
    new_events = []
    for each in all_events:
        event = each['event']
        eid = event['id']
        start_date = datetime.strptime(event['start_date'].split(" ")[0], "%Y-%m-%d")
        if start_date > since_date:
            new_events.append(eid)
    return new_events

if __name__ == "__main__":
    # These are tests to make sure api is working correctly.
    assert len(get_new_subscribers(11666856883)) == 4, "wrong number of subscribers for event 11666856883"
    assert len(set([9933187431, 9996671313, 9855257340, 10278722937, 10361963913, 10074712737, 10341105525, 10405742857, 10697070225, 10625203269, 10637411785, 10741037733, 10815137367, 10734815121, 10361207651, 10818894605, 10941635727, 10840130121, 11082589323, 11130101433, 11112069499, 10829891497, 11133315045, 11200199097, 11443968217, 11484216601, 11522721771, 11517546291, 11522765903, 11501847335, 11666856883, 11319740649, 11662923117, 11811593795, 10946672793]).intersection(get_events_for_year(2014))) == 35, "wrong number of events since 1/1/2014 to 5/31/2014"

