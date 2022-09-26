import json
import pprint
import sys

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from datetime import datetime

data_start = datetime.now()
# Step 0 - define path and driver
path = "/Users/mateusz/Documents/Code/related/chromedriver"
driver = webdriver.Chrome(path)

# Step 1 - get to site
driver.get("https://olx.pl")
time.sleep(2)


def main():
    early_steps()
    current_site_operation()
    save_collected_data()
    finish()


def separator(text):
    print(20 * "-")
    print(text)
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
    renting_category = driver.find_element(By.CLASS_NAME, "css-pyvavn")
    renting_category.click()
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


def current_site_operation():
    # waiting for site to load up
    time.sleep(3)
    # !! __NEXT PAGE__ !!
    # classify the html position for next page button
    next_page = driver.find_element(By.CLASS_NAME, "pagination-list")\
        .find_element(By.CSS_SELECTOR, 'a[data-cy="pagination-forward"]')
    print(next_page.get_attribute("href"))
    # input()
    # make sure site is loaded
    time.sleep(3)
    # classify the link part of offers
    offers = driver.find_elements(By.CLASS_NAME, "css-19ucd76")
    # create list of links
    links_from_current_site = []
    time.sleep(3)
    for offer in offers:
        try:
            link = offer.find_element(By.TAG_NAME, "a").get_attribute("href")
            links_from_current_site.append(link)
        except:
            pass
    iteration_and_window_handle(links_from_current_site)
    while True:
        try:
            next_page.click()
            time.sleep(3)
            current_site_operation()
        except:
            save_collected_data()
            finish()
            break


def iteration_and_window_handle(links_from_current_site):
    for link in links_from_current_site:
        # open new window
        time.sleep(2)
        current_window = driver.current_window_handle
        driver.switch_to.new_window()
        time.sleep(2)
        driver.get(link)
        time.sleep(2)
        get_data_of_listing()
        # wait for site to close
        time.sleep(2)
        driver.close()
        time.sleep(2)
        driver.switch_to.window(current_window)
        time.sleep(2)


listings = []


def get_data_of_listing():
    #click on certain offer
    time.sleep(3)
    try:
        get_from_olx()
    except:
        pass


def get_from_otodom():
    ...


def get_from_olx():
    listing = {}
    price = driver.find_element(By.CLASS_NAME, "css-dcwlyx")
    listing["rent"] = price.text
    date_n_tile = driver.find_elements(By.CLASS_NAME, "css-sg1fy9")
    date = date_n_tile[0]
    listing["publish-date"] = date.text.lstrip("Dodane")
    title = date_n_tile[1]
    listing["title"] = title.text
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
    time.sleep(2)
    separator("data collected correctly")
    pprint.pprint(listing)
    time.sleep(2)


def save_collected_data():
    with open("collected september 26th/original-data/original-data-26.json", "w") as json_file:
        json.dump(listings, json_file, indent=2)


def finish():
    question = input("Quit? ").upper()
    if question == "Y":
        driver.quit()
    data_finish = datetime.now()
    time = data_finish - data_start
    print(f"[{time.seconds}s]")
    sys.exit()


if __name__ == '__main__':
    main()
