'''
This script uses the AT Protocol Python SDK to get all valid records from a given List item.
It uses the Request library to send custom header request to ignore the timeout rules to help with large lists (10k+ records)
Invalid records (deleted Accounts etc) will be skipped as they do not return the expected response.
'''

from atproto import Client, Request
import os
from dotenv import load_dotenv
import csv
from time import sleep

load_dotenv()
request = Request(timeout=None)

userName = os.getenv('myUser')
myPassword = os.getenv('myPassword')

#need the list AT record, tools like pdsls.dev can easily return this for your own account lists
myList = os.getenv(<env variable>)

def main():
    '''
    must pass in pds url unless you are on bsky.social

    Example: for users on myatproto.social, it is hosted on the Blacksky PDS
    Client('https://blacksky.app', request=request)
    '''
    client = Client(<pds url>, request=request)
    client.login(userName,myPassword)

    # initiate a tracker for the pagination cursor
    cursor = None

    with open(<filename>, 'w') as neededList:
        while True:
            response = client.app.bsky.graph.get_list({'list': myModList, 'cursor': cursor, 'limit': 100})  #limit must be between 0-100, defaults to 50
            newitems = response.items
            for item in newitems:
                 blockList.write(item.subject.did + ',\n')
            old_cursor = cursor
            cursor = response.cursor
            # check cursor against old to protect against infinite loops
            if not cursor or (cursor == old_cursor):
                break

if __name__ == '__main__':
    main()