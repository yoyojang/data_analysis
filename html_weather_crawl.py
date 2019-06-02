import urllib.request as urlrequest
url_weather = 'http://www.weather.com.cn/weather/101190101.shtml'
web_page = urlrequest.urlopen(url_weather).read()
# print(web_page)

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_page,'html.parser')
forcast = soup.find(class_='t clearfix')
# print(forcast)
date_list = forcast.find_all('h1')
weather_list = forcast.find_all(class_='wea')
temp_list = forcast.find_all(class_='tem')
# windy_list = forcast.find_all('span')
# lvl_list = forcast.find_all('i')
# print(temp_list[0].get_text().replace('\n',''))
with open('weather_crawl.txt','w') as outputfile:
    for i in range(6):
        date = date_list[i].get_text()
        weather = weather_list[i].get_text()
        temp = temp_list[i].get_text().replace('\n','')
        # windy = windy_list[i].class_
        # lvl = lvl_list[i].get_text()
        # print('{} {} {} {} {}'.format(date,weather,temp,windy,lvl))
        outputfile.write('{} {} {}\n'.format(date, weather, temp))