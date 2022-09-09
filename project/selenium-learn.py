from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/Users/mateusz/Documents/Code/related/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        answear = article.find_element(By.CLASS_NAME, "entry-summary")
        print(answear.text)
        print()


finally:
    driver.quit()

print(datetime.now())
