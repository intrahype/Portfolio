<#
This is a Powershell script to use the XRPC endpoint on the ATProto PDS to get the CAR file 
backup for a given repo
#>

Invoke-WebRequest https://<pds.domain>/xrpc/com.atproto.sync.getRepo?did=did:plc:<user did here> -OutFile <\local\path\to\file\name.extension>