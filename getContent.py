import requests
from bs4 import BeautifulSoup as bs
import os


url = "https://www.gettyimages.ca/photos/kanye-west?family=editorial&phrase=kanye%20west&sort=mostpopular"

page = requests.get(url)
soup = bs(page.text, 'html.parser')

image_tags = soup.findAll('img')

if not os.path.exists('pictures'):
    os.makedirs('pictures')

os.chdir('pictures')

x = 0
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('Kanye-' + str(x) + '.jpg','wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x+=1
    except:
        pass

