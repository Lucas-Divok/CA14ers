# A data science project analyzing California's 15 highest peaks :D

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#these can change just chose random vv

plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")

print("California 14ers Analysis Project")

# California 14ers data from PeakBagger/SummitPost/MountainProject
# These are already ranked in order from highest to lowest 14er
# all the data for each peak matches like  line 21 matches with line 41/61 so on


ca_14ers_data = {
    'peak_name': [
        'Mount Whitney',
        'Mount Williamson',
        'White Mountain Peak',
        'North Palisade',
        'Starlight Peak',
        'Mount Shasta',
        'Mount Sill',
        'Polemonium Peak',
        'Mount Russell',
        'Split Mountain',
        'Middle Palisade',
        'Mount Langley',
        'Mount Muir',
        'Mount Tyndall',
        'Thunderbolt Peak'
    ],



    'elevation_ft': [
        14499,
        14379,
        14246,
        14245,
        14198,
        14162,
        14153,
        14104,
        14089,
        14060,
        14037,
        14033,
        14026,
        14023,
        14003
    ],



    'range': [
        'Sierra Nevada',
        'Sierra Nevada',
        'White Mountains',
        'Sierra Nevada',
        'Sierra Nevada',
        'Cascade Range',
        'Sierra Nevada',
        'Sierra Nevada',
        'Sierra Nevada',
        'Sierra Nevada',
        'Sierra Nevada',
        'Sierra Nevada',
        'Sierra Nevada',
        'Sierra Nevada',
        'Sierra Nevada'
    ],



    'prominence_ft': [
        10079,
        1721,
        7196,
        2894,
        124,
        9762,
        402,
        204,
        1105,
        1535,
        1158,
        1184,
        316,
        1113,
        275
    ],



    'difficulty_class': [
        '1',
        '3',
        '1',
        '4',
        '5',
        '3',
        '3',
        '4',
        '3',
        '3',
        '2',
        '1',
        '3',
        '2',
        '5'
    ],



    'route_distance_miles': [
        22.0,
        27.5,
        14.0,
        22.5,
        22.5,
        12.0,
        22.5,
        22.5,
        21.5,
        14.0,
        20.0,
        22.0,
        22.0,
        20.0,
        22.5
    ],



    'elevation_gain_ft': [
        6100,
        8000,
        3400,
        6000,
        6000,
        7200,
        6500,
        6000,
        6000,
        8100,
        6700,
        5100,
        5700,
        8000,
        6000
    ],



    'best_months': [
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'May-July',
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'July-Sept',
        'July-Sept'
    ],



    'latitude': [
        36.57861,
        36.65593,
        37.634144,
        37.09424,
        37.09508,
        41.408982,
        37.096006,
        37.09331,
        36.590004,
        37.02092,
        37.07055,
        36.52346,
        36.564751,
        36.655627,
        37.09755
    ],



    'longitude': [
        -118.29203,
        -118.31121,
        -118.255718,
        -118.51444,
        -118.51528,
        -122.194926,
        -118.503327,
        -118.5122,
        -118.291012,
        -118.42245,
        -118.46937,
        -118.23944,
        -118.291389,
        -118.336941,
        -118.51764 
    ]
}

# create DataFrame
df = pd.DataFrame(ca_14ers_data)

# convert difficulty class to numeric class (Yoesemite Decimal System)
df['difficulty_numeric'] = df['difficulty_class'].astype(int)

# making sure code is working
print(f"We have {len(df)} California 14ers to analyze.")

# print first 5 peaks to show our code works
print("\n First look at our peaks:")
print(df[['peak_name', 'elevation_ft', 'range', 'difficulty_class','route_distance_miles']].head())

# shape should return 15(names) and 10 + 1 (YDS) (subsections/identifiers)
print(f"Shape: {df.shape}")

# list columns to make sure its correct
print(f"Columns: {list(df.columns)}")

# show different data types
print(f"Data types:\n{df.dtypes}")

# STAGE 2 DATA ANALYSIS


#peak_name', 222


#elevation_gain_ft', most elev gain? least elev gain? avg elv gain?


#best_months', 

#latitude', 'longitude', 

#difficulty_numeric'

