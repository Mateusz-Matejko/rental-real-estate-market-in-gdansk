import json
import pprint

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

data_start = datetime.now()
# Step 0 - define path and driver
path = "/Users/mateusz/Documents/Code/related/chromedriver"
driver = webdriver.Chrome(path)

# Step 1 - get to site
driver.get("https://olx.pl")
time.sleep(2)


def main():
    early_steps()
    middle_steps()
    finish()


def separator(teks):
    print(20 * "-")
    print(teks)
    print(20 * "-")


def early_steps():
    # Step 2 - search for certain thing
    cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    try:
        cookies.click()
    except:
        pass
    # What do you search?
    search = driver.find_element(By.NAME, "q")
    search.send_keys("Mieszkania na wynajem")
    time.sleep(1)
    # Chose category
    search_by_category = driver.find_element(By.CLASS_NAME, "c000")
    search_by_category.click()
    time.sleep(1)

    # Chose closer category
    rent_category = driver.find_element(By.CLASS_NAME, "css-pyvavn")
    rent_category.click()
    time.sleep(2)

    # Chose city
    city = driver.find_element(By.CLASS_NAME, "css-kt3c71")
    city.click()
    time.sleep(1)
    city.send_keys("Gdańsk")
    time.sleep(2)

    # submit city
    city_submit = driver.find_element(By.CLASS_NAME, "css-1t10lps")
    city_submit.click()
    time.sleep(1)

    # submit choice
    submit = driver.find_element(By.NAME, "searchBtn")
    submit.click()
    time.sleep(1)


listings = []


def middle_steps():
    time.sleep(3)
    offers = driver.find_elements(By.CLASS_NAME, "css-19ucd76")
    time.sleep(3)
    for offer in offers:
        try:
            offer.click()
        except:
            try:
                next_page = driver.find_element(By.CLASS_NAME, "css-pyu9k9")
                next_page.click()
                middle_steps()
            except:
                separator("Can't click that shit")
        listing = {}
        #click on certain offer
        time.sleep(3)
        price = driver.find_element(By.CLASS_NAME, "css-dcwlyx")
        listing["Price"] = price.text
        date_n_tile = driver.find_elements(By.CLASS_NAME, "css-sg1fy9")
        date = date_n_tile[0]
        listing["Date"] = date.text.lstrip("Dodane ")
        title = date_n_tile[1]
        listing["Title"] = title.text
        listing["link"] = driver.current_url
        # description = driver.find_element(By.CLASS_NAME, "css-g5mtbi-Text")
        # listing["Opis"] = description.text
        options = driver.find_elements(By.CLASS_NAME, "css-ox1ptj")
        for option in options:
            try:
                k, v = option.text.split(":")
                listing[k] = v
            except:
                listing[option.text] = "Tak"
        listings.append(listing)
        time.sleep(5)
        driver.back()
        separator("done correctly")
        time.sleep(5)


def finish():
    question = input("Quit? ").upper()
    if question == "Y":
        driver.quit()
    data_finish = datetime.now()
    time = data_finish - data_start
    print(f"[{time.seconds}s]")


if __name__ == '__main__':
    main()
