#!/bin/bash

# <pds.domain> --replace with pds url, if you are using Bluesky PDS, enter bsky.social
# <user account did> --replace with account did (decentralized identity document), can be found using tools like pdsls.dev

# This is a simple retrival script using the XRPC endpoint for getRepo
# which will download the CAR file for a specified account

# This targets only Linux based systems with Bash installed
# while the same command can be used on MacOS, it requires extra configuration for wget and the zsh shell

wget https://<pds.domain>/xrpc/com.atproto.sync.getRepo?did=did:plc:<user account did>