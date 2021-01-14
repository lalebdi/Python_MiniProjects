from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/loaialebdi/Dev/Python_MiniProjects/seleniumToDict/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("Natasha")

l_name = driver.find_element_by_name("lName")
l_name.send_keys("blah")

email = driver.find_element_by_name("email")
email.send_keys("google")


search = driver.find_element_by_name("search")
search.send_keys("Natasha")
search.send_keys(Keys.ENTER)

# driver.close()
