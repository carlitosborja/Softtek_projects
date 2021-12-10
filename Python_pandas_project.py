#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd



def detect_change(df, date_col, was_rainy_col):
    
    """
    
    This function detects the day in which the weather turned rainy, and returns these dates in a pandas DataFrame structure.
    
    
    Parameters
    ---------------------
    
    df            :   pandas DataFrame. 
                      DataFrame with at least a date-like column and a column indicating if the weather was rainy. 
    
    date_col      :   string
                      Name of the DataFrame date column (not necessary to be a Timestamp type).
    
    was_rainy_col :   string
                      Name of the DataFrame column that indicates the weather for each day.
    
    """
    
    df_change = df[[date_col, was_rainy_col]][df[was_rainy_col].astype(int).diff() == 1]
    
    return df_change



def seasons(date):
    
    """
    
    Returns the season of the year for the date passed as the argument.
    
    
    Parameters
    ------------------
    
    date  :  Tiemstamp 
             Date that will be maped to its respective season of the year.
    
    """
    
    if pd.to_datetime(str(date.year) + '/3/19', format='%Y/%m/%d') <= date < pd.to_datetime(str(date.year) + '/6/20', format='%Y/%m/%d'):
        
        return 'spring'
    
    elif pd.to_datetime(str(date.year) + '/6/20', format='%Y/%m/%d') <= date < pd.to_datetime(str(date.year) + '/9/22', format='%Y/%m/%d'):
        
        return 'summer'
    
    elif pd.to_datetime(str(date.year) + '/9/22', format='%Y/%m/%d') <= date < pd.to_datetime(str(date.year) + '/12/21', format='%Y/%m/%d'):
        
        return 'fall'
    
    else:
        
        return 'winter'
    
    
    
def overall_status(items_status):
    
    """
    
    Rturns the overall status of an online order (can be of various items) based on the order status of each item individually.
    
    The status of each item can be: SHIPPED, PENDING or CANCELLED, and the overall status will be as the following statements:
    
    *if there is at least one item with PENDING status, the overall status will be PENDING
    
    *the overall status will be SHIPPED if all items have SHIPPED status or if there are only items with other status equal to CANCELLED
    
    *the overall status will be CANCELLED if and only if all items have CANCELLED status 
    
    
    Parameters
    ----------------
    
    items_status   :  array-like or list
                      Vector with all the items status. The item status are strings: 'SHIPPED', 'PENDING' or 'CANCELLED'
    
    """
    
    if 'PENDING' in items_status:
        return 'PENDING'
    
    elif 'SHIPPED' not in items_status:
        return 'CANCELLED'
    
    else:
        return 'SHIPPED'
    
    
    
def order_status(df, order_number_col, item_status_col):
    
    
    """
    
    This functions uses the overall_status function and applies it to a padas DataFrame. 
    
    Returns a pandas DataFrame that contains the order_numer of the online orders and their overall status.
    
    
    Parameters
    ---------------
    
    df      : pandas DataFrame
    
    order_number_col   :   string
                           Column name of column with the online order number
    
    item_status_col    :   string
                           Column name of the column with the status for each item 
    
    """
    
    df_ord_status = df.groupby(order_number_col)[item_status_col].apply(list).apply(overall_status)
    
    df_ord_status = df_ord_status.to_frame(name='status')
    
    return df_ord_status

