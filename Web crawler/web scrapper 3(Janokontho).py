from bs4 import BeautifulSoup as soup
import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from datetime import date

today = date.today()

url = 'https://www.dailyjanakantha.com/online/'

categories = ['sports', 'international', 'trade', 'science', 'lifestyle', 'job-news', 'culture']

firefox = wd.Firefox(executable_path = r'C:\Users\hp\Anaconda3\pkgs\geckodriver-0.28.0-h39d44d4_0\Scripts\geckodriver.exe')

for category in categories:

	firefox.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

	firefox.get(url+category)

	html = firefox.execute_script('return document.documentElement.outerHTML')

	parsedHtml = soup(html, 'html.parser')

	D = list()
	headlines = list()
	brief = list()
	topic = list()

	for news in parsedHtml.find_all('div', {'class':'list-article'}):
#		print(news.h2.text)
#		print(news.p.text)
#		print('<end>')
		if news.h2 is None or news.p is None: continue
		D.append(today)
		headlines.append(news.h2.text)
		brief.append(news.p.text[news.p.text.find('॥')+2:])
		topic.append(category)

	df = pd.DataFrame({'Date':D,'Category':topic, 'Headline': headlines, 'Brief News': brief})
	df.to_csv('Categorized_News_Data_set_2(janakontho).csv', mode = 'a', header = False, encoding='utf-8-sig')

	firefox.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
firefox.close()