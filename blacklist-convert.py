from urllib.request import urlopen
import os
import pandas as pd
import ipaddress
from ipaddress import IPv4Network, IPv4Address
import sys
# 
blocklist_url = sys.argv[1]

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

with urlopen( blocklist_url ) as file:
    content = file.read()
# Save to file.
with open( 'output.csv', 'wb' ) as output:
    output.write( content )

#delete lines starting by hastag
file1 = open('output.csv','r')
file2 = open('output2.csv','w')

for line in file1.readlines():
    if not (line.startswith('#')):
        # storing only those lines that
        # do not begin with "TextGenerator"
        file2.write(line)

# close and save the files
file2.close()
file1.close()

#extract DB name from URL
sub1 = "master/"

# getting index of substrings
if blocklist_url.endswith('.netset'):
    sub2 = ".netset"
    idx1 = blocklist_url.index(sub1)
    idx2 = blocklist_url.index(sub2)
    res = ''
# getting elements in between
    for idx in range(idx1 + len(sub1), idx2):
        res = res + blocklist_url[idx]
else: 
    sub2 = ".ipset"
    idx1 = blocklist_url.index(sub1)
    idx2 = blocklist_url.index(sub2)
    res = ''
# getting elements in between
    for idx in range(idx1 + len(sub1), idx2):
        res = res + blocklist_url[idx]

print(res)

#add first line
prepend_line("output2.csv", "ip")

#add new column for name
df = pd.read_csv("output2.csv")
for i in df['ip']:
        if '/' not in i :
            df['ip'] = df['ip']+''+'/32'
df['index'] = df.index + 1
df["name"] = res + df['index'].map(str)
df.to_csv(res+".csv", index=False)

#this is for the v2 :)
last_element = df["index"].iloc[-1]
#print(last_element)

os.remove("output.csv")
os.remove("output2.csv")
