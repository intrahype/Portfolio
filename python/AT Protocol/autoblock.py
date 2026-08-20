'''
This function uses the AT Protocol client and models libraries from the Python SDK 
to write new individual block records for an account.

It uses a csv file of individual DIDs and creates a simple log text file with the CID
and URI of each completed record for easy verification
'''


from atproto import Client, Request, models
from dotenv import load_dotenv
from time import sleep
import os
from pathlib import Path

#load env file for credentials
load_dotenv()

#set request to not timeout
request = Request(timeout=None)
#load credentials
userName = os.getenv('myUser')
myPassword = os.getenv('myPassword')
myDid = os.getenv('myDid')
#load directory path for file, this is not necessary for most local runs, but helps with venv's and wsgi configs
main_dir = Path(__file__).parent
filepath = main_dir / <filename>

def main():
    #login to PDS, must be passed in as uses bsky.app as default
    client = Client(<pds url>)
    client.login(userName,myPassword)


    with open('<logfile.txt>', 'w') as block_logfile:
        #open text file to keep track of each create record
        counter = 1 #counter to use as variable for log file
        with open(filepath, 'r') as modList:
            #readlines includes commas and new line notation, hence later slice of [:-2]
            did_list = modList.readlines()
            for item in did_list:
                clean_did = item[:-2]   #clean up DID for record, not necessary if DID already in 'did:plc:<identifier>' format

                #create block record using Python SDK for AT Protocol
                block_record = models.AppBskyGraphBlock.Record(
                    subject = clean_did,
                    created_at = client.get_current_time_iso(),
                )

                #send block record to api for write
                blocked = client.app.bsky.graph.block.create(myDid, block_record)

                #write counter, CID, and URI of created record
                block_logfile.write(f'Created Block Item {counter}: CID={blocked.cid}; URI={blocked.uri}\n')
                counter += 1

                #sleep between requests depending on usage, sleep(8) ensures a 24 hour run that does not exceed Bluesky API limits
                sleep(8)

        #close any open files to save RAM
        <filename>.close()
    block_logfile.close()   

if __name__ == '__main__':
    main()