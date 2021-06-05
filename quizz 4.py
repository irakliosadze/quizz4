import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint


file = open('myauto.csv', 'w', newline='\n')
# file.write('Name,Year,Price\n')
file_obj1 = csv.writer(file)
file_obj1.writerow(['Name', 'Year', 'Price'])

p = {'groups': 'hyundai', 'start': 1}
h= {'Accept-Language': 'en-US'}
ind = 1
url = 'https://www.myauto.ge/ka/s/0/0/16/00/2012/00/2/00/iyideba-hyundai-2012-geo?stype=0&for_rent=0&marka=16&year_from=2012&price_from=4000&price_to=7000&currency_id=1&fuel_type_id=2&customs_passed=1&loc_id=2&det_search=0&ord=7&keyword='

while p['start']<251:
     r = requests.get(url, headers={'user-agent':'Chrome '})
     r = requests.get(url, params=p, headers=h)
     # print(r.url)
     content = r.text
     soup = BeautifulSoup(content, 'html.parser')
     block = soup.find('div', class_='search-lists-container')
     all_cars = block.find_all('div', class_='current-item-inner')

     for each in all_cars:
         name = each.h4.a.text
         year = each.find('span', class_='car-levy car-year').text
         year = year.replace(')', '')
         year = year.replace(')', '')
         price = each.find('span', class_='car-price ').text
         print(price)
         # file.write(name + ',' + year + ',' + price + '\n')
         file_obj1.writerow([name, year, price])

    p['start'] += 50
    sleep(randint(15,20))

file.close()







