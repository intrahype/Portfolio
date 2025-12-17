# This script will find differences between two csv files text strings
# and write any missing lines to a new file

#import csv module
import csv

# use open method to instantiate both files
# replace filenames with local files, files must be in same folder as script file
with open('<filename>', 'r') as f1, open('<filename2>', 'r') as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()

# use open method to iterate through both files looking for matches
# write non-matches to new file
with open('<outputfilename>', 'w') as difference_file:
    for line in f1_lines:
        if line not in f2_lines:
            difference_file.write(line)