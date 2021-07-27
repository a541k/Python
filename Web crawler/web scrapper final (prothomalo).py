from bs4 import BeautifulSoup as soup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date

today = date.today()

url = 'https://www.prothomalo.com/'
categories = ['sports', 'chakri', 'lifestyle', 'opinion', 'entertainment', 'business', 'world', 'politics', 'bangladesh']

#open firefox
driver = webdriver.Firefox(executable_path=r'C:\Users\hp\Anaconda3\pkgs\geckodriver-0.28.0-h39d44d4_0\Scripts\geckodriver.exe')


for category in categories:


	#selenium requires geckodriver as interface to run firefox
	#needed chromedriver if chosen browser is chrome
	#open tab
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
	#load url
	driver.get(url+category)

	#execute js in the browser and return html
	page = driver.execute_script('return document.documentElement.outerHTML')
	#parsing the html
	selSoup = soup(page, 'html.parser')

	headlines = list()
	brief     = list()
	topic     = list()
	D = list()

	for news in selSoup.find_all('div', class_='customStoryCard9-m__story-data__2qgWb'):
#		print(news.h2.text+'>')
#		print(news.span.text)
#		print('_'*8)

		#empty element exception, produces error in .text portion
		if news.h2 is None or news.span is None: continue

		#all data found in single page in each iteration
		headlines.append(news.h2.text)
		brief.append(news.span.text)
		topic.append(category)
		D.append(today)

	df = pd.DataFrame({'Date':D, 'Category':topic, 'Headline':headlines, 'Brief News': brief})
	df.to_csv('Categorized_News_Data_set.csv', mode = 'a', header = False, encoding='utf-8-sig')#utf-8 gave error

	#close tab
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')#close
#	print(news.text[:-12])
#	file =
#	file.write(news.text)
#file.close()

#close firefox
driver.close()

