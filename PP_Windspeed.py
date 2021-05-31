#!/usr/bin/env/Python3

# data location on my local machine: SOKOTRA (Mac)
location = '/Users/jminz/Documents/Project/MPI-DTU Python Code/Agora-Offpot/Post_Processed_Data/wind_speeds/Denmark'


#import required modules
import os
import pandas as pd
import numpy as np
import glob

# navigate to directory containing original data 
os.chdir(location)

# no wind farm data case or CTRL 
NOWF_df = pd.read_csv('NOWF_hourly_time_date_U_V.csv')
NOWF_df.drop(columns = ['Unnamed: 0', 'Unnamed: 0.1','Time.1'], inplace = True )

# calculate wind speeds
NOWF_df['ws_mpers_CTRL'] = np.sqrt(NOWF_df['U_mpers']**2 + NOWF_df['V_mpers']**2)

# calculate wind directions with north as 0 degrees
NOWF_df['ws_dir_degree_CTRL'] = np.mod(90 + np.arctan2(NOWF_df['V_mpers'],NOWF_df['U_mpers'])*(180/np.pi),360)

degrees = [
(NOWF_df['ws_dir_degree_CTRL']> 0) & (NOWF_df['ws_dir_degree_CTRL'] <= 22.5), #North
(NOWF_df['ws_dir_degree_CTRL']> 337.5) & (NOWF_df['ws_dir_degree_CTRL'] <= 360.0), # North
(NOWF_df['ws_dir_degree_CTRL']> 157.5) & (NOWF_df['ws_dir_degree_CTRL'] <= 202.5), # South
(NOWF_df['ws_dir_degree_CTRL']> 57.5) & (NOWF_df['ws_dir_degree_CTRL'] <= 112.5), # West
(NOWF_df['ws_dir_degree_CTRL']> 242.5) & (NOWF_df['ws_dir_degree_CTRL'] <= 292.5), # East
(NOWF_df['ws_dir_degree_CTRL']> 292.5) & (NOWF_df['ws_dir_degree_CTRL'] <= 337.5), # North East
(NOWF_df['ws_dir_degree_CTRL']> 22.5) & (NOWF_df['ws_dir_degree_CTRL'] <= 57.5), # North West
(NOWF_df['ws_dir_degree_CTRL']> 112.5) & (NOWF_df['ws_dir_degree_CTRL'] <= 157.5), # South West
(NOWF_df['ws_dir_degree_CTRL']> 202.5) & (NOWF_df['ws_dir_degree_CTRL'] <= 242.5) # South East
    ]
directions = ['North',
              'North',
              'South',
              'West',
              'East', 
              'North_East',
              'North_West',
              'South_West',
              'South_East']

NOWF_df['dirn_CTRL'] = np.select(degrees, directions)
NOWF_df['scenario'] = 'CTRL'
NOWF_df['date'] = pd.to_datetime(NOWF_df['date'], format = '%Y-%m-%d')
NOWF_df = NOWF_df.sort_values(by=['date','Time'])
NOWF_df.to_csv('sorted_CTRL_hourly_time_date_U_V.csv')

# for wind park cases 

# look for files with the wind parks 
list_of_df = ['_D1A1','_D2A1','_D1A3','_D2A3','_D3A3']
load_df = []
for i in glob.glob('Denmark*.csv'):
    load_df.append(i)
    
for ix,file in enumerate(load_df):
    df = pd.read_csv(file)
    df.drop(columns = ['Unnamed: 0', 'Unnamed: 0.1','Time.1'], inplace = True )
    df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')
    df['ws_mpers_'+str(load_df[ix].split('_')[1])] = np.sqrt(df['U_mpers']**2 + df['V_mpers']**2)
    df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] = np.mod(90 + np.arctan2(df['V_mpers'],df['U_mpers'])*(180/np.pi),360)
    degrees = [
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 0) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 22.5), #North
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 337.5) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 360.0), # North
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 157.5) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 202.5), # South
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 57.5) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 112.5), # West
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 242.5) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 292.5), # East
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 292.5) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 337.5), # North East
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 22.5) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 57.5), # North West
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 112.5) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 157.5), # South West
    (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])]> 202.5) & (df['ws_dir_degree_'+str(load_df[ix].split('_')[1])] <= 242.5) # South East
        ]
    directions = ['North',
                  'North',
                  'South',
                  'West',
                  'East', 
                  'North_East',
                  'North_West',
                  'South_West',
                  'South_East']
    df['dirn_'+str(load_df[ix].split('_')[1])] = np.select(degrees, directions)
    df = df.sort_values(by=['date','Time'])
    df.to_csv('sorted_'+file)
    
