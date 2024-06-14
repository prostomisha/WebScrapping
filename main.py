import requests
from bs4 import BeautifulSoup

''' parser of the website https://news.ycombinator.com/ which extracts the first 30 entries 
taking only the number, the title, the points, and the number of comments for each entry and 
filtering all previous entries with more than five words in the title ordered by 
the number of comments first
and filtering all previous entries with less than or equal to five words in the title ordered by points.
'''

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
news_list = soup.find_all('tr', class_='athing')
for news in news_list:
    news_number = news.find('span', class_='rank').get_text()
    news_title = news.find('span', class_='titleline').get_text()
    # news_points = news.find('span', class_='').get_text()
    # news_comments = news.find('span', class_='').get_text()
    print(news_number, news_title)
