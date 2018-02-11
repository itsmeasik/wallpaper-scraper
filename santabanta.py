import requests
import urllib
from bs4 import BeautifulSoup

name = str(input("Enter Celebrity Name(Capitalize Each Word Like This,Examples: Gal Gadot, Katrina Kaif)\n"))
l_name = name.lower()
l_name = l_name.replace(" ", "-",)
print(name)
#print(type(l_name))

page = 1
i = 0
while True:
    url_add = 'http://www.santabanta.com/wallpapers/' + str(l_name) + '/?page=' + str(page)
    # print(url_add)
    source_code = requests.get(url_add)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    check = str(soup.findAll('a', {'title': str(name)}))
    #print(check)
    if check != "[]":
        for link in soup.findAll('a', {'title': str(name)}):
            # print(link)
            href = 'http://www.santabanta.com' + link.get('href')
            # print(href)
            if 'photo' in href:
                # print(href)
                url = str(href) + '?high=6'
                # print(url)
                source_code = requests.get(url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, 'html.parser')
                for link in soup.find('div', {'class': 'wallpaper-big-1-downloads'}):
                    href1 = link.get('href')
                    # print(href1)
                    i += 1
                    print('downloading wallpaper' + str(i))


                    def download_web_image(url):
                        file_name = str(name) + '_' + str(i)
                        file_name = str(file_name) + '.jpg'
                        urllib.request.urlretrieve(url, file_name, )


                    download_web_image(href1)
    else:
        print("Stop")

        break

    page += 1
print("Rerun & Enter Other Name")