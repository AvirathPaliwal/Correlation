import plotly.express as px
import csv
import numpy as np


def getDataSource( data_path):
     icecreamSales = []
     coldDrinksSales= []
     with open(data_path) as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
               icecreamSales.append( float(row["Temperature"]))
               coldDrinksSales.append(float(row["Ice-cream Sales"]))
     return { "x" : icecreamSales , "y" : coldDrinksSales}

def findCorrelation(datasource):
     correlation = np.corrcoef( datasource["x"] , datasource["y"])
     print(correlation[0,1])

def setup():
     dp = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
     ds = getDataSource( dp ) 
     findCorrelation(ds)

setup()
