import pandas as pd

def coffee_data(df):

  columns = ['address','city','state','latitude','longitude','stars','review_count','is_open','Coffee & Tea',
      'Cafes',
      'Restaurants',
      'Breakfast & Brunch',
      'Bakeries',
      'Desserts',
      'Grocery',
      'Specialty Food',
      'Convenience Stores',
      'Coffee Roasteries',
      'Food Trucks',
      'Bars',
      'Donuts',
      'Bagels']
  df = df[columns]
  
  coffee_columns = ['Coffee & Tea',
      'Cafes',
      'Restaurants',
      'Breakfast & Brunch',
      'Bakeries',
      'Desserts',
      'Grocery',
      'Specialty Food',
      'Convenience Stores',
      'Coffee Roasteries',
      'Food Trucks',
      'Bars',
      'Donuts',
      'Bagels']
  df = df[coffee_columns + ['address','city','state','latitude','longitude','stars','review_count','is_open']]
  condition = (df[coffee_columns] == 1).any(axis=1)
  df = df[condition]
  
  df_coffee_tea = df[(df['Coffee & Tea']>0) & (df['is_open']>0)]

return df_coffee_tea
