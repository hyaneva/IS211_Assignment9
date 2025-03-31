
#Import libraries
import requests
from bs4 import BeautifulSoup



#Link being scraped - https://finance.yahoo.com/quote/AAPL/history/?p=AAPL



#Set headers and url to be scraped
headers =  {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/XXX Safari/537.36"
}
url = 'https://finance.yahoo.com/quote/AAPL/history/?p=AAPL'



#Collect page of Apple stock list
response = requests.get(url, headers=headers)

#Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')



#Find the table containing player stats
table = soup.find("table")

#Get all rows except the header
rows = table.find_all("tr")[1:]



#Print the header
print(f"{'Date':<15}{'Close Price':<10}")

#Extract and print stock data
for row in rows:
    cols = row.find_all("td")

    #Ensures row has enough columns (because some rows might be empty)
    if len(cols) >= 5:
        date = cols[0].text.strip()  # Date column
        close_price = cols[4].text.strip()  # Closing price column

    #Prints formatted output
    print(f"{date:<15}{close_price:<10}")



