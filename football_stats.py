

#Import libraries
import requests
from bs4 import BeautifulSoup


#Link being scraped - https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/

#Set headers and url to be scraped
headers =  {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/XXX Safari/537.36"
}
url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/'





#Collect first page of NFL list
response = requests.get(url, headers=headers)

#Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')





#Find the table containing player stats
table = soup.find("table")

#Get all rows except header
rows = table.find_all("tr")[1:21]  # Top 20 players





#Print the header
print(f"{'Player':<25}{'Position':<12}{'Team':<8}{'TDs':<5}")

#Extract and print player stats
for row in rows:
    cols = row.find_all("td")
    
    #The first column contains player, position, and team as a single string
    player_info = cols[0].text.strip().split()

    #Extract player name (first and last)
    player_name = " ".join(player_info[4:6]) 
    position = player_info[-2]  #Second to last item (position)
    team = player_info[-1]  #Last item (team)

    td = cols[8].text.strip()  #Touchdowns column

    #Print the cleaned up player information with fixed alignment
    print(f"{player_name:<25}{position:<12}{team:<8}{td:<5}")
