from selenium import webdriver

chrome_driver_path = "/Users/loaialebdi/Dev/Python_MiniProjects/seleniumToDict/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


driver.close()
