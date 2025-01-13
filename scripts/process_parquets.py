import pyarrow.parquet as pa 
import pandas as pd
import numpy as np
import os
from pandas import DataFrame



def process_dataframe(df: DataFrame) -> DataFrame:
    # convert ns to s
    df['time_of_day'] = df['time_of_day'] / (10 ** 9) # convert ns to s

    # get day number for aggregation
    pass 

def get_clean_df(df: DataFrame, item_id:str) -> DataFrame:
    # add 'day_number' to dataframe
    # add 'user_id to dataframe

    df_temp = df.copy()
    df_temp['day_change'] = df_temp['weekday'].ne(df_temp['weekday'].shift(1))
    # Explanation: 
    #   .shift(1) looks at the previous row’s day_of_week
    #   .ne(...) means "not equal" (True if they differ, False if they’re equal)

    # 2) Build a day_number by taking the cumulative sum of these changes.
    #    We fill missing values for the first row with False and then add 1.
    df_temp['day_change'] = df_temp['day_change'].fillna(False)
    df_temp['day_number'] = df_temp['day_change'].cumsum()

    df_temp['user_id'] = item_id
    
    return df_temp

# get daily light ans steps
def get_daily_light_and_steps(df: DataFrame) -> DataFrame:
    df_daily_light = pd.DataFrame(df.groupby(['day_number','weekday'], as_index=False)
                                  .aggregate({'light': 'mean', 'enmo': 'sum'})
                                .rename(columns={'light': 'daily_light_mean', 'enmo': 'daily_steps'}))

    return df_daily_light

def get_daily_steps(df: DataFrame) -> DataFrame:
    df_daily_steps = pd.DataFrame(df.groupby(['day_number','weekday'])['enmo'].sum())
    pass 
    return df_daily_steps


def read_parquet_files(data_directory='data') -> DataFrame:
    
    data_dir = 'data'
    steps_light_df = pd.DataFrame()

    for item_name in os.listdir(data_dir):
        item_path = os.path.join(data_dir, item_name)

        if os.path.isdir(item_path) and item_name.startswith("id="):
            item_id = item_name.split("=")[1]
            parquet_file_path = os.path.join(item_path, 'part-0.parquet')
            
            if os.path.exists(parquet_file_path):
                print(f"Now processing: {parquet_file_path}")
                
                df = pd.read_parquet(parquet_file_path)
                df = get_clean_df(df, item_id=item_id)
                
                # print(df.head())
                daily_lights = get_daily_light_and_steps(df)
                print(daily_lights.shape)
                daily_lights['user_id'] = item_id
                # print(daily_lights)
                steps_light_df = pd.concat([steps_light_df, daily_lights])
                
                del df
    return steps_light_df


# if __name__ == '__main__':
#     result = read_parquet_files(data_directory='../data')
#     print(result.shape)
#     print(result)
#     result.to_csv('steps_light.csv', index=True)