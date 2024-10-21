import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"E:\AIBSS\Datasets\Amazon Sales Data\amazon.csv")
pd.set_option('display.max_columns', None)

#shape of Dataset
print(f"Number of rows are {df.shape[0]}\nNumber of columns are {df.shape[1]}")

#checking Datatype of Columns
print(f"Datatypes of attributes are {df.info()}")

#checking for Null values
print(f"Check for Null Values\nNull Values are:{df.isnull().sum()}")

#Chanaging Datatype to Float
df['discounted_price'] = df['discounted_price'].str.replace("₹", '')
df['discounted_price'] = df['discounted_price'].str.replace(",", '')
df['discounted_price'] = df['discounted_price'].astype('float')
df['actual_price'] = df['actual_price'].str.replace("₹", '')
df['actual_price'] = df['actual_price'].str.replace(",", '')
df['actual_price'] = df['actual_price'].astype('float')
df["discount_percentage"] = df["discount_percentage"].str.replace("%", '')
df["discount_percentage"] = df["discount_percentage"].astype('float')
df["discount_percentage"] = df["discount_percentage"]/100
df['rating'] = df['rating'].str.replace('|', '3.9').astype('float64')
df['rating_count'] = df['rating_count'].str.replace(',', '').astype('float64')

#Replacing missing values with mean
df['rating_count'] = df['rating_count'].fillna(df['rating_count'].mean())

#checking for Null values again
print(f"Check for Null Values\nNull Values are:{df.isnull().sum()}")

#loading clean data into another csv
df.to_csv("cleaned_data.csv")