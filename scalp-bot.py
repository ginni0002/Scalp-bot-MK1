import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.get("https://www.bestbuy.com/site/microsoft-bluetooth-mouse-matte-black/6379633.p?skuId=6379633")
browser.maximize_window()

SelectCountryButton = browser.find_element_by_link_text("United States")
SelectCountryButton.click()

notFound = True
while notFound:

    addToCartButton = browser.find_element_by_class_name("add-to-cart-button")
    print("true")
    

    if ( "disabled_mu48L" in addToCartButton.get_attribute("class") ):
        time.sleep(5)
        print("disabled")
        browser.refresh()

    else:
        notFound = False


addToCartButton.click()

# Waiting for the popup to appear and then closing it

wait = WebDriverWait(browser,10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'attach-suggestion-component')))
popupClose = browser.find_element_by_class_name("close-modal-x")
popupClose.click()

cartButton = browser.find_element_by_id("shop-cart-icon-9579b869-6276-480a-9e8a-a9761e1ed581")
cartButton.click()

checkoutButton = browser.find_element_by_class_name('btn-lg')

checkoutButton.click()




