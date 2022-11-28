import requests
import pandas as pd
# url = 'https://api.exchangerate.host/latest'
# response = requests.get(url)
# data = response.json()
#
# print(data)
# print(len(data['rates']))
#
#

url = 'https://www.x-rates.com/table/?from=USD&amount=1'
response = requests.get(url).content
raw_data = pd.read_html(response)
data = raw_data[-1]
print(data)

data.to_csv("country_name.csv")
