import pandas as pd
import numpy as np
import requests
import csv
import sqlite3
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# since sqlite is a light database we will be using this to store our data
# connecting to database
connection = sqlite3.connect(r'./facilities.db')
logging.info('Database connected successfully')
# get the data from url

def get_resources():
    logging.info('Getting resources ')

    url = "https://json.link/PKXTD7Z0il.json"
    data = requests.get(url)
    Data = data.json()
    return Data['results']

# write into csv
def writetocsv(data: list):
    logging.info('Converting to csv ')

    all_keys = set().union(*(d.keys() for d in data))
    with open('facilities.csv', 'w+') as f:
        w = csv.DictWriter(f, all_keys)
        w.writeheader()
        w.writerows(data)


def csv_to_sql():
    logging.info('Generating SQL database')

    # load the csv
    facilities_data = pd.read_csv('facilities.csv')
    # write to sql database
    facilities_data.to_sql('facilities', connection,
                           if_exists='replace', index=False)


def validation_sql():
    # create cursor then fetch the data in database
    cur = connection.cursor()
    for row in cur.execute('SELECT * FROM facilities'):
        print(row)


if __name__ == "__main__":
    writetocsv(get_resources())
    csv_to_sql()
    # validation_sql()
    connection.close()
    logging.info('Done')
