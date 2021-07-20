from bs4 import BeautifulSoup
import lxml

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