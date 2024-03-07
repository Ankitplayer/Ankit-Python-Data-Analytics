import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import os

def load_data():
    df = pd.read_excel('Canada.xlsx',
                       sheet_name=1,
                       skiprows=20,
                       skipfooter=2)
    
    cols_to_drop = ['AREA', 'REG', 'DEV', 'Type', 'Coverage']
    df = df.drop(cols_to_drop, axis=1, inplace=True)

    df = df.rename(columns={
        'OdName' : 'country',
        'AreaName' : 'continent',
        'RegName' : 'region',
        'DevName' : 'status',
    })
    years = list(range(1980, 2014))
    df['total'] = df[years].sum(axis=1)
    df.set_index('country', inplace=True)
    return df