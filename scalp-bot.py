import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

browser.get("https://www.bestbuy.com/site/microsoft-arc-touch-mouse-black/1261563.p?skuId=1261563")
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

cartButton = browser.find_element_by_class_name("shop-cart-icon")
cartButton.click()

checkoutButton = browser.find_element_by_class_name('btn-lg')

checkoutButton.click()

element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'guest')))
ContinueAsGuestButton = browser.find_elements_by_tag_name("button")[4]
ContinueAsGuestButton.click()


element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'form-group')))
input_mapping = {'user.emailAddress':"sekhonginni0002@gmail.com" , 'user.phone':"+919877969404"}

for key,value in input_mapping.items():
    

    text_input = browser.find_element_by_id(key)
    
    text_input.send_keys(value)

ContinuePayementInfo = browser.find_element_by_class_name('btn-lg')
ContinuePayementInfo.click()

wait = WebDriverWait(browser,10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'mini-footer')))

time.sleep(10)
formGroupInst = browser.find_elements_by_class_name('form-control')
formList = ['1234 5678 9101 2131','Khush Harman Singh','Sekhon','112th St St Albert','Louisinia','FL','160062']
for ch in range (len(formGroupInst)-3) :
    formGroupInst[ch].clear()
    formGroupInst[ch].send_keys(formList[ch])
 
#Address 
addressField = browser.find_element_by_id('payment.billingAddress.street')
addressField.send_keys('Jackson Ashville some random hood street')

#hide-suggestions
hideSuggestionButtion = browser.find_element_by_class_name('autocomplete__toggle')
hideSuggestionButtion.click()

#City
CityField = browser.find_elements_by_class_name('form-control')[4]
CityField.send_keys('Adams')

#State 
sel = Select(browser.find_element_by_class_name('smart-select'))
sel.select_by_visible_text("OR")

#Zip Code
ZipField = browser.find_elements_by_class_name('form-control')[5]
ZipField.send_keys('97810')








