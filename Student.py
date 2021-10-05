import plotly.express as px
import csv
import numpy as np


def getDataSource( data_path):
     marks_In_Percentage = []
     days_Present= []
     with open(data_path) as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
               marks_In_Percentage.append( float(row["Marks In Percentage"]))
               days_Present.append(float(row["Days Present"]))
     return { "x" : marks_In_Percentage , "y" : days_Present}

def findCorrelation(datasource):
     correlation = np.corrcoef( datasource["x"] , datasource["y"])
     print(correlation[0,1])

def setup():
     dp = "Student Marks vs Days Present.csv"
     ds = getDataSource( dp ) 
     findCorrelation(ds)

setup()

