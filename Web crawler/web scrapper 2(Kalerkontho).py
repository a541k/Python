from bs4 import BeautifulSoup as soup
import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from datetime import date


url = 'https://www.kalerkantho.com/online/'
today = str(date.today())

categories = ['world','entertainment', 'sport', 'business', 'info-tech', 'lifestyle', 'readers-place']

firefox = wd.Firefox(executable_path = r'C:\Users\hp\Anaconda3\pkgs\geckodriver-0.28.0-h39d44d4_0\Scripts\geckodriver.exe')

for category in categories:
	firefox.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'t')
	firefox.get(url+category)
	html = firefox.execute_script('return document.documentElement.outerHTML')
	parsedHTML = soup(html,'html.parser')

	headlines = list()
	brief     = list()
	topic     = list()
	D = list()

	for news in parsedHTML.find_all('div',{'class':'col-xs-12 col-sm-6 col-md-6 n_row'}):
#		print(news.a.text)
#		print(news.p.text)
#		print('<end>')
		if news.a is None or news.p is None: continue
		#exception
		headlines.append(news.a.text)
		brief.append(news.p.text)
		topic.append(category)
		D.append(today)

	df = pd.DataFrame({'Date': D, 'Category':topic , 'Headline':headlines, 'Brief News': brief})
	df.to_csv('Categorized_News_Data_set_2(kalerkontho).csv', mode = 'a', header = False, encoding='utf-8-sig')

	firefox.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')

firefox.close()


