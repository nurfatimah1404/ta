from datetime import datetime

bs = './data/lab/1/bs.csv'
server = 'data/lab/1/server.csv' 

f = open(bs, 'r').read().splitlines()

print("anu")
for line in f:
    print(line)