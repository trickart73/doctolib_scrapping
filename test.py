from email import header
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://www.youtube.com/watch?v=U6gbGk5WPws&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=3&ab_channel=TechWithTim

PATH = "C:\Program Files\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# driver.get("https://www.techwithtim.net/")
driver.get("https://www.doctolib.fr/psychiatre/lyon/helene-huon-de-penanster/")
# driver.get("https://www.schlouk-map.com/fr/cities/lyon")


def getNamesForArticles(driver):
    try:
        allSearchResult = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "results"))
    )
        carton = allSearchResult.find_elements_by_class_name("dl-search-result-name")
        for aTag in carton:
            print(aTag.text)
    finally:
        driver.quit()
        print("end")


print(driver.title)

# Good practice : wait the element exist before 
try:
    elementOui = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "dl-selectable-card-title"))
    )
    # print(element.text)
    elementOui.click()
finally:
        # driver.quit()
        print("elementOui")

try:
    elementAuCabinet = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "dl-radio-button-label-text"))
    )
    elementAuCabinet.click()
finally:
        print("elementAuCabinet")

try:
    elementBookingMotive = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "booking_motive"))
    )
    # print(elementBookingMotive.text)
    elementBookingMotive.click()
    elementBookingMotive.send_keys(Keys.DOWN)
    elementBookingMotive.send_keys(Keys.DOWN)
    elementBookingMotive.send_keys(Keys.ENTER)
finally:
        print("elementBookingMotive")


try:
    elementDispo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "availabilities-message"))
    )
    # print(elementDispo.text)
    # buttonDispo = elementDispo.find_elements(by=By.CLASS_NAME, value="dl-button-link-primary")
    # buttonDispo.click()
    # elementDispo.click()
finally:
        print("elementDispo")

# try:
#     elementDispo = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "availabilities-slot"))
#     )
#     print(elementDispo.get_attribute("title"))
#     # buttonDispo = elementDispo.find_elements(by=By.CLASS_NAME, value="dl-button-link-primary")
#     # buttonDispo.click()
#     # elementDispo.click()
# finally:
#         print("elementDispo")



# driver.quit()



# print(driver.page_source) => entire source code for the page

# driver.close() => close the tab
# driver.quit() => close the browser

### Find link by name
# link = driver.find_element_by_link_text("En savoir plus")
# link.click()
