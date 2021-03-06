import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()


def YearlyPrice(fueltype):
    """
    Function that outputs a box & whisker plot of fuel prices in 2016, 2017 & 2018 based on fueltype
       
       fueltype - any fuel type recorded in Fuel Check data:
                    U91, PDL, P98, P95, LPG, E85, E10, DL, B20
    """
    #import data
    fuel2016 = pd.read_csv('fuel_data/fuel2016.csv')
    fuel2017 = pd.read_csv('fuel_data/fuel2017.csv')
    fuel2018 = pd.read_csv('fuel_data/fuel2018.csv')
    
    #select relevant information & clean up data
    type_2016 = fuel2016[fuel2016['FuelCode']==fueltype]
    type_2017 = fuel2017[fuel2017['FuelCode']==fueltype]
    type_2018 = fuel2018[fuel2018['FuelCode']==fueltype]
    
    #plot in box & whisker graph
    y0 = type_2016['Price'].tolist()
    y1 = type_2017['Price'].tolist()
    y2 = type_2018['Price'].tolist()

    trace0 = go.Box(y=y0,
                    name=str(fueltype+' Prices 2016'),
                    marker= dict(color='#c0d6e4')
                   )
    trace1 = go.Box(y=y1,
                    name=str(fueltype+' Prices 2017'),
                    marker= dict(color='#6897bb')
                   )
    trace2 = go.Box(y=y2,
                    name=str(fueltype+' Prices 2018'),
                    marker=dict(color='#455890')
                   )

    data = [trace0, trace1, trace2]
    layout = go.Layout(
        title='Annual Price of '+str(fueltype),
        yaxis=dict(
            title='Price (cpl)')
    )
    
    fig = go.Figure(
        data=data,
        layout=layout)
    
    iplot(fig)

YearlyPrice('E10')
