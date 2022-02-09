import pandas as pd
import numpy as np
import requests
# get the data from url
url = "https://json.link/nToM1Rrccn.json"
data = requests.get(url)
Data = data.json()
Data = Data['results']

# write into csv
def writetocsv(p):
  with open('student.csv', 'w+') as f: 
    w = csv.DictWriter(f, p.keys())
    w.writeheader()
    w.writerow(p)
length = len(Data)
columns = data
for i in range(length):
  p = Data[i]
  writetocsv(p)