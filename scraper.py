from bs4 import BeautifulSoup, Comment
import requests
import pandas as pd
import urllib.request, json
from datetime import date

#Obtaining todays date

today = date.today()
# print('Today:',today)

#dd-mm-yyy
dd_mm_yyyy = today.strftime("%d-%m-%Y")
# print("Date Format 1: =", dd_mm_yyyy)

##dd-mmm-yyyy
dd_MMM_yyyy = today.strftime("%d-%b-%Y")
# print("Date Format 2: =", dd_MMM_yyyy)


# To Obtain raw HTML content
url = "https://www.mohfw.gov.in/data/datanew.json"
html_content = requests.get(url).content

#LATEST COVID DATA
with urllib.request.urlopen("https://www.mohfw.gov.in/data/datanew.json") as url:
    data = json.loads(url.read().decode())
    # df = pd.read_json(url)
    # print(df)

daily = pd.DataFrame(data).sort_values(by='state_name',ascending=True)
daily.to_csv('C:\\Users\\HP\\Documents\\Data Scraped For COVID\\'+dd_MMM_yyyy+'.csv')



# SCRAPING TESTING DATA
url = "https://www.icmr.gov.in/"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
div_html = soup.find_all("div", class_= "scf-text")

num = []
for item in div_html:
    x = item.find('h2')
    num.append(x.text.replace('\n',' ').strip())


for i, n in enumerate(num):
    x = n.strip()
    x = x.replace(",", "")
    num[i] = int(x)
num.append(dd_mm_yyyy)
totals = []
totals.append(num)

output_file_name_2 = dd_MMM_yyyy
daily_test = pd.DataFrame(totals,columns = ['CUMULATIVE TOTAL SAMPLES TESTED','NO OF SAMPLES TESTED','DATE'])
daily_test.set_index('DATE',inplace=True)
daily_test.to_csv('C:\\Users\\HP\\Documents\\Data Scraped For COVID\\'+output_file_name_2+'(Testing).csv')