# Script to go through a given directory recusively and remove files based on file extension

import os

""" 
Directory path should be formatted as follows:
 '<disk>:/path/to/file
 Windows example: C:/Users/test/testUser/Downloads 
 MacOS example: /Volume/folderName
"""

directoryToUse = <insert path to top folder here>

for subdir, dirs, files in os.walk(directoryToUse):
    for file in files:
        if file.endswith("<add file extension in quotes"):
            #os.remove or os.unlink both work here as their functionality is identical, remove comes from windows, unlink from UNIX
            os.remove(os.path.join(directoryToUse, subdir, file))
