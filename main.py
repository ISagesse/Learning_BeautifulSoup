from bs4 import BeautifulSoup
import requests

respons = requests.get('https://news.ycombinator.com/')
yc_webpage = respons.text
soup = BeautifulSoup(yc_webpage, 'html.parser')

articles = soup.find_all(name='a', class_='storylink')
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)
















with open("website.html",encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())

# a = soup.find_all(name='a')
# for tag in a:
    # print(tag.getText())
    # print(tag.get('href'))
# print(a)

# heading = soup.find(name='h1', id='name')
# print(heading)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name)

heading = soup.select_one(selector='.heading')
print(heading)
