from Modules.Utils.add_df import coffee_data
import pandas as pd

def filtered_data(df):
  
  df_coffee_tea = coffee_data(df)

  df_coffee = df_coffee_tea.reset_index()
  
  df_speciality = df_coffee[~df_coffee['name'].str.contains('Starbucks', case=False)]
  df_speciality = df_speciality[~df_speciality['name'].str.contains('Dunkin', case=False)]
  df_speciality = df_speciality[~df_speciality['name'].str.contains('McDonald', case=False)]

  def categorize(row):
    if row['Cafes'] > 0:
        return 'Cafes'
    elif row['Restaurants']  > 0:
        return 'Restaurants'
    elif row['Breakfast & Brunch']  > 0:
        return 'Breakfast & Brunch'
    elif row['Bakeries']  > 0:
        return 'Bakeries'
    elif row['Desserts']  > 0:
        return 'Desserts'
    elif row['Specialty Food']  > 0:
        return 'Specialty Food'
    elif row['Convenience Stores']  > 0:
        return 'Convenience Stores'
    elif row['Coffee Roasteries']  > 0:
        return 'Coffee Roasteries'
    elif row['Food Trucks']  > 0:
        return 'Food Trucks'
    elif row['Bars']  > 0:
        return 'Bars'

    else:
        return 'Other'

    df_specialty_new['Category'] = df_speciality.apply(categorize, axis=1)
    
    def category(row):
        if row['Coffee & Tea'] > 0:
            return 'Coffee & Tea'
    
    df_specialty_new['Main_Category'] = df_specialty_new.apply(category, axis=1)
    
  
    return df_specialty_new

  
