from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/loaialebdi/Dev/Python_MiniProjects/seleniumToDict/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com")


all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Natasha")
search.send_keys(Keys.ENTER)

# driver.close()
