from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

import login
import Interactions
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

login.login(driver)

locator = ""

filter_manager_cloumn_last_opened = ""
filter_manager_dropdown_item_index = 1

column_to_open = ""
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
time.sleep(1)
# Clicking navigation: Purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
time.sleep(1)
# Clicking navigation: All purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
time.sleep(1)
# ❌ Locator not found for: No Control Name (Type: )
# Clicking button: SystemDefinedNewButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
# Inputting into: PurchTable_OrderAccount
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "1001")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "1001")
# Clicking button: OK
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Clicking (default) on: SystemDefinedOptions
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='SystemDefinedOptions']")
# ❌ Locator not found for: LineSpec (Type: grid)
# Inputting into: PurchLine_ItemId
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "1000")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "1000")
# Inputting into: InventoryDimensionsGrid_InventSiteId
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "4")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "4")
# Inputting into: InventoryDimensionsGrid_InventLocationId
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "48")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "48")
# ❌ Locator not found for: GridInventLocation (Type: grid)
# ❌ Locator not found for: GridInventLocation (Type: grid)
# Clicking button: SystemDefinedSaveButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
# Clicking (default) on: Purchase
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Purchase']")
# Clicking (default) on: buttonConfirm
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='buttonConfirm']")
time.sleep(5)
print("test case passed")
driver.quit()