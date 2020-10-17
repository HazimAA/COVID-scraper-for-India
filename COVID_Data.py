import requests
import pandas as pd
import urllib.request, json

pd.set_option('display.max_columns',None)
pd.set_option('display.width', 250)

# loading json into dataframe method
url = "https://api.covid19india.org/v4/timeseries.json"
df = pd.read_json(url, orient = 'index')#.sort_values(by ='dates', axis=0, ascending=True)

df2 = pd.DataFrame(df['dates'].values.tolist(), index=df.index)

#Saving Daily Totals for the whole Country
df.to_csv('C:\\Users\\HP\\Documents\\Total COVID data accumulated by someone, scraped by me\\Daily_Totals_Latest_Country.csv')
df2.to_json(r'C:\Users\HP\Documents\Total COVID data accumulated by someone, scraped by me\JSON Daily_Totals_Latest_Country')