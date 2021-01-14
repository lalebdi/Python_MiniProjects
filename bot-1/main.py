from selenium import webdriver

chrome_driver_path = "/Users//Dev/Python_MiniProjects/bot-1/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

# driver.close()
driver.quit()