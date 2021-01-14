from selenium import webdriver

chrome_driver_path = "/Users/loaialebdi/Dev/Python_MiniProjects/bot-1/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.apple.com")

# driver.close()
driver.quit()