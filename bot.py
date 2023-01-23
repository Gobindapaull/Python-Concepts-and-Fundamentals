import pandas as pd
from datetime import date as dt

def pos_calc():
    df = pd.DataFrame()
    adding_pos = True

    while adding_pos == True:
        temp_df = pd.DataFrame()
        today = dt.today()
        temp_df['date'] = [today]
        asset_name = input('enter the asset name : ')
        temp_df['asset_name'] = [asset_name]
        asset_price = input(f'enter the {asset_name} price : ')
        asset_price = round(float(asset_price), 2)

        print({asset_name})
        print({asset_price})

pos_calc()

#enter the asset name : bitcoin
#enter the bitcoin price : 30000
#{'bitcoin'}
#{30000.0}
