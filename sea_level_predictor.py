import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv(
        'C:/Users/Davie/Documents/GitHub/freeCodeCamp/data/epa-sea-level.csv')

    # define data
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(x, y, color='green')

    # Get slope, intercept from linregress
    res = linregress(x, y)

    # Create first line of best fit
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, color="black")

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    res_2000 = linregress(x_2000, y_2000)
    x_pred2000 = pd.Series([i for i in range(2000, 2051)])
    y_pred2000 = res_2000.intercept + res_2000.slope * x_pred2000
    plt.plot(x_pred2000, y_pred2000, color="red")

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()

# using statsmodel

from datetime import datetime
dates = sm.tsa.datetools.dates_from_range('1880', length=len(df.Year))
df['Year']=dates
df
#df = df.set_index('Year')
dates = pd.date_range("1880", periods=len(df.Year), freq="A-DEC")
dates
#df.index = pd.to_datetime(df.index)
x=pd.Series(dates)
x