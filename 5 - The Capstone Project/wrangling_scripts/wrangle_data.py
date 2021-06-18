import pandas as pd
import plotly.graph_objs as go
#from myapp.routes import my_form_post
# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`
#text = my_form_post()
def readdata(dataset):
    """Clean Melbourne data for a visualizaiton dashboard

   

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """    
    df = pd.read_csv(dataset)


    return df


def plot_first(df):

    df_t = df['surface']
    return df_t


def plot_first_two(df):
    u = df['surface'].value_counts().index
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

df_train = readdata('data/X_train.csv')
df_test = readdata('data/X_test.csv')
df_target = readdata('data/y_train.csv')
#  series_0 = df_train[df_train['series_id'] == 0]
def return_figures(number):
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    series_0 = df_train[df_train['series_id'] == number]
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = [x for x in range(len(series_0['orientation_W']))],
      y = series_0['orientation_W'],
      
      )
    )

    layout_one = dict(title = 'The distribution of orientation_W in series number {}'.format(number),
                xaxis = dict(title = 'Orientation_W',),
                yaxis = dict(title = 'Distribution'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []

    graph_two.append(
      go.Scatter(
      x = [x for x in range(len(series_0['orientation_X']))],
      y = series_0['orientation_X'],
      )
    )

    layout_two = dict(title = 'The distribution of orientation_X in series number {}'.format(number),
                xaxis = dict(title = 'Orientation_X',),
                yaxis = dict(title = 'Distribution'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
        x=[x for x in range(len(series_0['orientation_Y']))],
        y=series_0['orientation_Y'],
      
      )
    )

    layout_three = dict(title = 'The distribution of orientation_Y in series number {}'.format(number),
                xaxis = dict(title = 'Orientation_Y'),
                yaxis = dict(title = 'Distribution')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []

    
    graph_four.append(
      go.Scatter(
      x =[x for x in range(len(series_0['orientation_Z']))],
      y = series_0['orientation_Z'],

      )
    )

    layout_four = dict(title = 'The distribution of orientation_Z in series number {}'.format(number),
                xaxis = dict(title = 'Orientation_Z'),
                yaxis = dict(title = 'Distribution'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures