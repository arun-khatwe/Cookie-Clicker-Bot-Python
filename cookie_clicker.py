from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


import time


# Set up the ChromeDriver path
chromedriver_path = r"C:\Users\ROOT\Desktop\chromedriver\chromedriver.exe" 


# Set up the chrome options
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


# Create a new instance of the chrome driver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)


# Navigate to the website
driver.get("https://orteil.dashnet.org/cookieclicker/")


# https://orteil.dashnet.org/cookieclicker/


cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"


WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'English')]"))
)


language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)


cookie = driver.find_element(By.ID, cookie_id)


while True:
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.ID, cookie_id))
    )
    cookie.click()
    cookies_count = int(driver.find_element(By.ID, cookies_id).text.replace(",", "").split(" ")[0])


    for i in range(15): 
        try:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, product_price_prefix + str(i)))
            )
            product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
            if not product_price.isdigit():
                continue
            product_price = int(product_price)
            if cookies_count >= product_price:
                product = driver.find_element(By.ID, product_prefix + str(i))
                product.click()
                break
        except:
            continue