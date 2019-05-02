import pandas as pd
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()
import matplotlib.pyplot as plt


#Import data & establish variables for use in function 

###  1 - Income Data  ###
raw_data = pd.read_csv('income_data/total income 2010-11 to 2015-16.csv')
    
#select data for just Sydney Regions
syd_data = raw_data.iloc[15:29]

#clean data
syd_data["Unnamed: 31"] = syd_data["Unnamed: 31"].str.replace(",","").astype(float)
syd_data["Unnamed: 25"] = syd_data["Unnamed: 25"].str.replace(",","").astype(float)
syd_data = syd_data.drop(columns=['Earners (persons)','Unnamed: 3','Unnamed: 4','Unnamed: 5',
                                  'Unnamed: 6','Unnamed: 7','Median age of earners (years)',
                                  'Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12',
                                  'Unnamed: 13','Income ($)','Unnamed: 15','Unnamed: 16',
                                  'Unnamed: 17','Unnamed: 18','Unnamed: 19','Median ($)',
                                  'Unnamed: 21','Unnamed: 22','Unnamed: 23','Unnamed: 24',
                                  'Mean ($)','Unnamed: 27','Unnamed: 28',
                                  'Unnamed: 29','Unnamed: 30'],axis=1)
syd_data = syd_data.rename(columns={'Unnamed: 0': 'SA4','Unnamed: 1': 'SA4 NAME',
                                    'Unnamed: 25':'Median ($) 2015-16','Unnamed: 31':'Mean ($) 2015-16'})

#create lists from data
name = syd_data['SA4 NAME'].tolist()
income = syd_data['Mean ($) 2015-16'].tolist()
incomemedian = syd_data['Median ($) 2015-16'].tolist()


### 2 - Fuel Price Data ###
postcodes = pd.read_csv('SEIFA_data/1270055006_CG_POSTCODE_2011_SA4_2011.csv')
postcodes.drop(columns=['POSTCODE.1','RATIO','PERCENTAGE'],inplace=True)

#import fuel data
fuel2016 = pd.read_csv('fuel_data/fuel2016.csv')
e10_2016 = fuel2016[fuel2016['FuelCode']=='E10']

#sort postcodes by SA4 Region 
baulkham = postcodes[postcodes['SA4_CODE_2011']==115]
blacktown = postcodes[postcodes['SA4_CODE_2011']==116]
city = postcodes[postcodes['SA4_CODE_2011']==117]
eastern_sub = postcodes[postcodes['SA4_CODE_2011']==118]
innersouthwest = postcodes[postcodes['SA4_CODE_2011']==119]
innerwest = postcodes[postcodes['SA4_CODE_2011']==120]
northsyd = postcodes[postcodes['SA4_CODE_2011']==121]
northbeaches = postcodes[postcodes['SA4_CODE_2011']==122]
outersouthwest = postcodes[postcodes['SA4_CODE_2011']==123]
outerwest = postcodes[postcodes['SA4_CODE_2011']==124]
parramatta = postcodes[postcodes['SA4_CODE_2011']==125]
ryde = postcodes[postcodes['SA4_CODE_2011']==126]
southwest = postcodes[postcodes['SA4_CODE_2011']==127]
sutherland = postcodes[postcodes['SA4_CODE_2011']==128]

#create lists of postcodes per region
city_pc = city['POSTCODE'].tolist()
baulkham_pc = baulkham['POSTCODE'].tolist()
blacktown_pc = blacktown['POSTCODE'].tolist()
eastern_sub_pc = eastern_sub['POSTCODE'].tolist()
innersouthwest_pc = innersouthwest['POSTCODE'].tolist()
innerwest_pc = innerwest['POSTCODE'].tolist()
northsyd_pc = northsyd['POSTCODE'].tolist()
northbeaches_pc = northbeaches['POSTCODE'].tolist()
outersouthwest_pc = outersouthwest['POSTCODE'].tolist()
outerwest_pc = outerwest['POSTCODE'].tolist()
parramatta_pc = parramatta['POSTCODE'].tolist()
ryde_pc = ryde['POSTCODE'].tolist()
southwest_pc = southwest['POSTCODE'].tolist()
sutherland_pc = sutherland['POSTCODE'].tolist()

#group fuel price by SA4 Sydney Region 
city_2016 = e10_2016[e10_2016['Postcode'].isin(city_pc)]
baulkham_2016 = e10_2016[e10_2016['Postcode'].isin(baulkham_pc)]
blacktown_2016 = e10_2016[e10_2016['Postcode'].isin(blacktown_pc)]
eastern_sub_2016 = e10_2016[e10_2016['Postcode'].isin(eastern_sub_pc)]
innersouthwest_2016 = e10_2016[e10_2016['Postcode'].isin(innersouthwest_pc)]
innerwest_2016 = e10_2016[e10_2016['Postcode'].isin(innerwest_pc)]
northsyd_2016 = e10_2016[e10_2016['Postcode'].isin(northsyd_pc)]
northbeaches_2016 = e10_2016[e10_2016['Postcode'].isin(northbeaches_pc)]
outersouthwest_2016 = e10_2016[e10_2016['Postcode'].isin(outersouthwest_pc)]
outerwest_2016 = e10_2016[e10_2016['Postcode'].isin(outerwest_pc)]
parramatta_2016 = e10_2016[e10_2016['Postcode'].isin(parramatta_pc)]
ryde_2016 = e10_2016[e10_2016['Postcode'].isin(ryde_pc)]
southwest_2016 = e10_2016[e10_2016['Postcode'].isin(southwest_pc)]
sutherland_2016 = e10_2016[e10_2016['Postcode'].isin(sutherland_pc)]

#calculate mean fuel price for each region
city_2016_mean = city_2016['Price'].mean()
baulkham_2016_mean = baulkham_2016['Price'].mean()
blacktown_2016_mean = blacktown_2016['Price'].mean()
eastern_sub_2016_mean = eastern_sub_2016['Price'].mean()
innersouthwest_2016_mean = innersouthwest_2016['Price'].mean()
innerwest_2016_mean = innerwest_2016['Price'].mean()
northsyd_2016_mean = northsyd_2016['Price'].mean()
northbeaches_2016_mean = northbeaches_2016['Price'].mean()
outersouthwest_2016_mean = outersouthwest_2016['Price'].mean()
outerwest_2016_mean = outerwest_2016['Price'].mean()
parramatta_2016_mean = parramatta_2016['Price'].mean()
ryde_2016_mean = ryde_2016['Price'].mean()
southwest_2016_mean = southwest_2016['Price'].mean()
sutherland_2016_mean = sutherland_2016['Price'].mean()

#calculate median fuel price for each region
city_2016_median = city_2016['Price'].median()
baulkham_2016_median = baulkham_2016['Price'].median()
blacktown_2016_median = blacktown_2016['Price'].median()
eastern_sub_2016_median = eastern_sub_2016['Price'].median()
innersouthwest_2016_median = innersouthwest_2016['Price'].median()
innerwest_2016_median = innerwest_2016['Price'].median()
northsyd_2016_median = northsyd_2016['Price'].median()
northbeaches_2016_median = northbeaches_2016['Price'].median()
outersouthwest_2016_median = outersouthwest_2016['Price'].median()
outerwest_2016_median = outerwest_2016['Price'].median()
parramatta_2016_median = parramatta_2016['Price'].median()
ryde_2016_median = ryde_2016['Price'].median()
southwest_2016_median = southwest_2016['Price'].median()
sutherland_2016_median = sutherland_2016['Price'].median()

#create list for plotting
fuelmeans = [baulkham_2016_mean,blacktown_2016_mean,city_2016_mean, eastern_sub_2016_mean,
             innersouthwest_2016_mean,innerwest_2016_mean,northsyd_2016_mean,northbeaches_2016_mean, 
             outersouthwest_2016_mean,outerwest_2016_mean,parramatta_2016_mean,ryde_2016_mean,
             southwest_2016_mean,sutherland_2016_mean
            ]

fuelmedian = [baulkham_2016_median,blacktown_2016_median,city_2016_median, eastern_sub_2016_median,
             innersouthwest_2016_median,innerwest_2016_median,northsyd_2016_median,northbeaches_2016_median, 
             outersouthwest_2016_median,outerwest_2016_median,parramatta_2016_median,ryde_2016_median,
             southwest_2016_median,sutherland_2016_median
            ]


def IncomeFuelSA4(FuelMeasure, IncomeMeasure):
    #define variables
    x = name
    
    if FuelMeasure == 'Mean':
        y = fuelmeans
    else:
        y = fuelmedian
    
    if IncomeMeasure == 'Mean':
        z = income
    else:
        z = incomemedian

    fig, ax1 = plt.subplots()
    plt.xticks(rotation=90, size=15)
    
    #duplicate axes with the same x axis and different y axis
    ax2 = ax1.twinx() 

    # plot data on axes 1, and 2
    trace1, = ax1.plot(x, 
                       y, 
                       label=str(FuelMeasure)+" E10 Price 2016", 
                       color='#c0d6e4',
                       marker='o', 
                       markersize='8'
                      )
    trace2, = ax2.plot(x, 
                       z, 
                       label=str(IncomeMeasure)+" Income 2015-16", 
                       color='#455890', 
                       marker='o', 
                       markersize='8'
                      )

    # Make a curves list to access the parameters in the curves
    traces = [trace1, trace2]

    # add legend 
    ax1.legend(traces, [trace.get_label() for trace in traces])
    
    #label y axes
    ax1.set_ylabel("Fuel Price (cpl)", size=15)
    ax2.set_ylabel("Income ($)", size=15)

    #global figure properties - format graph
    plt.title("Comparison of Fuel Prices and Income for SA4 Region", size = 20)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)

    #plot
    plt.show()
    
IncomeFuelSA4('Mean', 'Mean')
