import os
import eventbrite

EB_APP_KEY = os.environ['EB_APP_KEY']
EB_API_KEY = os.environ['EB_API_KEY']

FOR_YEAR = 2014

eid = 11666856883

eb_auth_tokens = {'app_key':  EB_APP_KEY, 'user_key':EB_API_KEY}
eb_client = eventbrite.EventbriteClient(eb_auth_tokens)

attendees = eb_client.event_list_attendees({"id":11666856883})['attendees']


#[0]['attendee']['answers'][0]['answer']['answer_text']

def get_new_subscribers(event_id)
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


