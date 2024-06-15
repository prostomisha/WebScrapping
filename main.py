import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime

''' parser of the website https://news.ycombinator.com/ which extracts the first 30 entries 
taking only the number, the title, the points, and the number of comments for each entry and 
filtering all previous entries with more than five words in the title ordered by 
the number of comments first
and filtering all previous entries with less than or equal to five words in the title ordered by points.
'''

url = 'https://news.ycombinator.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

entries = []

news_list = soup.find_all('tr', class_='athing')
subtext_list = soup.find_all('td', class_='subtext')

for index, (news, subtext) in enumerate(zip(news_list, subtext_list)):

    # extracting number
    news_number = news.find('span', class_='rank').get_text().strip('.')

    # title
    news_title = news.find('span', class_='titleline').find('a').get_text()

    # points
    news_points = subtext.find('span', class_='score')
    # if there is no points we set value to '0' (issue with one of the news)
    news_points2 = news_points.get_text().split()[0] if news_points else '0'

    # comments
    news_comments = subtext.find_all('a')[-1].get_text().split()[0]

    # If value of news_comments is 'discuss' change it to '0' for converting it to int after
    ''' One of the news from website was created incorrectly with only 2 fields (time and hide)
    The fastest way to solve is to check if the last element == 'hide' change it to '0' 
    New's article: "Nango (YC W23) Is Hiring a Senior Product Engineer (100% Remote)"
    '''
    if news_comments == 'discuss' or news_comments == 'hide':
        news_comments = '0'

    # structuring data to json format using dict
    entry = {
        'news_number': int(news_number),
        'news_title': news_title,
        'news_points': int(news_points2),
        'news_comments': int(news_comments),
    }
    #print(entry)

    # adding each dict to our list
    entries.append(entry)


# Filter all entries with more than five words in the title ordered by the number of comments first
def filter_entries(entries):

    # returns counted words without symbols
    def count_words(entry):
        words = re.findall(r'\b\w+\b', entry['news_title'])
        return len(words)

    # creating list with word count more than 5 and list with less or equal 5
    list1 = []
    list2 = []
    for entry in entries:
        if count_words(entry) > 5:
            entry.update({'filter': 'Sorted by comments'})
            entry.update({'timestamp': str(datetime.now())})
            list1.append(entry)
        elif count_words(entry) <= 5:
            entry.update({'filter': 'Sorted by points'})
            entry.update({'timestamp': str(datetime.now())})
            list2.append(entry)

    # sorting list ordered by the number of comments
    new_list1 = sorted(list1, key=lambda x: x['news_comments'], reverse=True)

    # sorting list ordered by points
    new_list2 = sorted(list2, key=lambda x: x['news_points'], reverse=True)

    return new_list1 + new_list2


sorted_list = filter_entries(entries)
print(sorted_list)
headers = ['news_number', 'news_title', 'news_points', 'news_comments', 'filter', 'timestamp']
df = pd.DataFrame(sorted_list, columns=headers)
print(df)
df.to_csv('news.csv')
