import requests
from bs4 import BeautifulSoup
import lxml
from fake_useragent import UserAgent
import csv
from openpyxl import load_workbook
from time import sleep

array = []

def set_sity_data(url):
	global kb
	global array
	try:
		ua = UserAgent()
		response = requests.get(url).text
		doma = BeautifulSoup(response, 'lxml').find('table', class_='table table-condensed table-hover table-striped').find('tbody').find_all('tr')
		for dom in doma:
			try:
				
				headers = {
					'user-agent': ua.random,
					'content-type': 'application/javascript' 
				}

				link_doma = 'https://dom.mingkh.ru' + dom.find_all('td')[1].find('a').get('href')

				response = requests.get(link_doma, headers = headers).text
				all_attrs = BeautifulSoup(response, 'lxml')
				dom_attrs = all_attrs.find('ul', class_='breadcrumb').find_all('li')
				try:
					republick = dom_attrs[1].text.strip()
					name_sity = dom_attrs[2].text.strip()
					name_ulica = dom_attrs[3].text.strip()
					number_ulica = all_attrs.find('div', class_='block-heading-two').text.split(',')[-1].replace('»', '').strip()
				except Exception as e:
					asferahgrt =1
				uk = 'Нет'
				uk_test = BeautifulSoup(response, 'lxml').find('dl', class_='dl-horizontal house').find_all('dt')
				for o in uk_test:
					try:
						if o.text == 'Управляющая компания':
							uk = all_attrs.find('dl', class_='dl-horizontal house').find_all('dd')[-2].find('span').text.replace('Ук', '')
							break
						else:
							uk = 'Нет'
						
					except Exception as e:
						continue

				perem = ''
				try:
					test_year = all_attrs.find('table', class_='table table-hover table-striped').find('thead').find('tr').find_all('th')
				except Exception as e:
					continue
				for i in test_year:
					if i.text == 'Год проведения':
						perem = 'yes'
						break
					else:
						perem = 'no'

				try:
					if perem == 'yes':
						attrs_kap = all_attrs.find('table', class_='table table-hover table-striped').find('tbody').find_all('tr')
						for kap_rem in attrs_kap:
							kap_rem = kap_rem.find_all('td')
							vid = kap_rem[0].text
							year = kap_rem[1].text

							sleep(0.5)
							with open('main.csv', 'a', newline='', encoding = 'utf-8') as f:
								writer = csv.writer(f, delimiter = '#')
								writer.writerow([republick, name_sity, name_ulica, number_ulica, uk, vid, year, link_doma])
							with open('main.txt', 'a') as r:
								r.write(f'{republick}, {name_sity}, {name_ulica}, {number_ulica}, {uk}, {vid}, {year}, {link_doma}\n')
							with open('test.csv', 'a', encoding= 'utf-8', newline='') as f:
								writer = csv.writer(f, delimiter = '#')
								writer.writerow([republick, name_sity, name_ulica, number_ulica, uk, vid, year, link_doma])
								
					elif perem == 'no':
						attrs_kap = all_attrs.find('table', class_='table table-hover table-striped').find('tbody').find_all('tr')
						for kap_rem in attrs_kap:
							kap_rem = kap_rem.find_all('td')
							vid = kap_rem[0].text
							year = 'Неизвестно'
							sleep(0.5)
							with open('main.csv', 'a', newline='', encoding = 'utf-8') as f:
								writer = csv.writer(f, delimiter = '#')
								writer.writerow([republick, name_sity, name_ulica, number_ulica, uk, vid, year, link_doma])
							with open('main.txt', 'a') as r:
								r.write(f'{republick}, {name_sity}, {name_ulica}, {number_ulica}, {uk}, {vid}, {year}, {link_doma}\n')
							with open('test.csv', 'a', encoding= 'utf-8', newline='') as f:
								writer = csv.writer(f, delimiter = '#')
								writer.writerow([republick, name_sity, name_ulica, number_ulica, uk, vid, year, link_doma])
								

					
				except Exception as e:
					rgvrtb = 1

			
				kb+=1
			except Exception as e:
				continue
	except Exception as e:
		print(e)