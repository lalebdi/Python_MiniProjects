from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/loaialebdi/Dev/Python_MiniProjects/seleniumToDict/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(article_count.text)

# article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Natasha")
search.send_keys(Keys.ENTER)

# driver.close()
