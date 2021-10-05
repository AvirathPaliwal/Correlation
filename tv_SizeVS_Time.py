import plotly.express as px
import csv

with open("Size of TV,_Average time spent watching TV in a week (hours).csv") as  csv_file:
     df = csv.DictReader(csv_file)
     fig = px.scatter( df, x = "Size of TV" , y = "\tAverage time spent watching TV in a week (hours)")
     #fig.show()

import numpy as np

def getDataSource(data_path):
    TV_Size = []
    Time_spent = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            TV_Size.append(float(row['Size of TV']))
            Time_spent.append(float(row['\tAverage time spent watching TV in a week (hours)']))
    
    return {'x':TV_Size , 'y':Time_spent}

def findcorrelatio(ds):
    c = np.corrcoef( ds['x'] , ds['y'])
    print(c[0,1])

def setup():
    dp = 'Size of TV,_Average time spent watching TV in a week (hours).csv'
    ds = getDataSource(dp)
    findcorrelatio(ds)

setup()

       
        


