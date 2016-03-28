import os
import mailchimp

MC_API_KEY = os.environ['MC_API_KEY']
mc_client = mailchimp.Mailchimp(MC_API_KEY)

def addSubscribers(list_id, subscribers):
    return mc_client.lists.batch_subscribe(list_id, subscribers, double_optin=False)

if __name__ == "__main__":
    pass

    
    
