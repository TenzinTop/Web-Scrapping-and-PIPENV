from selenium import webdriver
from datetime import time, datetime

#open up a browser and navigate to web page
driver = webdriver.Firefox(executable_path="C:\\Users\\Tenzin topgyal\\Desktop\\pipenv and web scraping\\geckodriver\\Web-Scrapping-and-PIPENV\\geckodriver.exe")
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

#extract list of buyers and prices as per on the web 
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

#printing the number of buyers along with its prices
num_page_items = len(buyers)
file = open("data.text",'w')

for i in range(num_page_items):
    file.write(buyers[i].text + " : " + prices[i].text)
    print(buyers[i].text + " : " + prices[i].text)

file.write("This was recorded on ",datetime.now())    

file.close()
driver.close()
