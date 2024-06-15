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
subtext_list = soup.find_all('td', class_='subtext')

for index, (news, subtext) in enumerate(zip(news_list, subtext_list)):
    news_number = news.find('span', class_='rank').get_text()
    news_title = news.find('span', class_='titleline').find('a').get_text()
    news_points = subtext.find('span', class_='score').get_text()
    news_comments = subtext.find_all('a')[-1].get_text()
    print(news_number, news_title, news_points, news_comments)


