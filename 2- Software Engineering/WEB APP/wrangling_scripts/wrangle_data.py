import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`
def cleandata(dataset):
    """Clean Melbourne data for a visualizaiton dashboard

   

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """    
    df = pd.read_csv(dataset)
    #We will be interested only in some columns:['Rooms', 'Price', 'Postcode', 'Type', 'Suburb','Date', 'Landsize']
    df = df[['Rooms', 'Price', 'Postcode', 'Type', 'Suburb', 'Date', 'Landsize']]
    #We will plot this 
    return df


def plot_first(df):
    """This function returns the mean of price grouped by Postcode"""
    mean_df_price = df.groupby('Postcode').mean()
    return mean_df_price['Price']


def plot_first_two(df):
    df = df.sort_values('Postcode', ascending=False) 
    u = df['Postcode'].sort_values().unique()
    return u

def plot_two(df):
    df['Date'] = pd.DatetimeIndex(df['Date']).year
    df_m = df[df['Suburb']=='Melbourne']
    df_m.pop('Type')
    df_m.pop('Rooms')
    df_m.pop('Postcode')
    df_m = df_m.groupby('Date').mean()
    return df_m['Price']

def plot_three(df):
    df_s = df[['Suburb', 'Price']]
    df_s = df_s.groupby('Suburb').max()
    return df_s['Price']

def plot_three_two(df):
    df_s = df[['Suburb', 'Price']]
    return df_s['Suburb'].sort_values().unique()

def plot_four(df):
    df_r = df[df['Suburb']=='Reservoir']
    return df_r

df = cleandata('data/melb_data.csv')

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    
    graph_one = []    
    graph_one.append(
      go.Bar(
      x = plot_first_two(df),
      y = plot_first(df),
      
      )
    )

    layout_one = dict(title = 'Mean of Price group by Postcode',
                xaxis = dict(title = 'Postcode',),
                yaxis = dict(title = 'Average price'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []

    graph_two.append(
      go.Bar(
      x = [2016, 2017], 
      y = plot_two(df),
      )
    )

    layout_two = dict(title = 'The average price in Melbourne in 2016 and 2017',
                xaxis = dict(title = 'Year',),
                yaxis = dict(title = 'Average price'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = plot_three(df),
      y = plot_three_two(df),
      
      )
    )

    layout_three = dict(title = 'Max values for prices in different Suburb',
                xaxis = dict(title = 'Max values'),
                yaxis = dict(title = 'Suburb')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    m = plot_four(df)
    
    graph_four.append(
      go.Scatter(
      x =m['Landsize'],
      y = m['Price'],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Prices based on landsize in Reservoir',
                xaxis = dict(title = 'Landsize'),
                yaxis = dict(title = 'Prices'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures