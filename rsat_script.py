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
user_input = None
"Skipping grid since it is deafault behavior of d365"
# Inputting into: PurchLine_ItemId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: PurchLine_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_ItemId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]", "Kit00002")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "Kit00002")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "Kit00002")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "Kit00002")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
# Inputting into: PurchLine_VariantId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_VariantId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Variant number')]") ):
    #clicking inside grid: PurchLine_VariantId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_VariantId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_VariantId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_VariantId')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Variant number')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Variant number')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Variant number')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_VariantId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_VariantId')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Variant number')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Variant number')]", "")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: InventoryDimensionsGrid_InventSiteId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
    #clicking inside grid: InventoryDimensionsGrid_InventSiteId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')])[1]", "5")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Site')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "5")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]", "5")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "5")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
# Inputting into: InventoryDimensionsGrid_InventLocationId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
    #clicking inside grid: InventoryDimensionsGrid_InventLocationId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')])[1]", "55")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Warehouse')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]", "55")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]", "55")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "55")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
# Inputting into: PurchLine_PurchUnitGrid
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchUnitGrid')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Unit')]") ):
    #clicking inside grid: PurchLine_PurchUnitGrid
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchUnitGrid')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_PurchUnitGrid')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchUnitGrid')])[1]", "pcs")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Unit')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Unit')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Unit')])[1]", "pcs")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchUnitGrid')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchUnitGrid')]", "pcs")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Unit')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Unit')]", "pcs")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
time.sleep(5)
print("test case passed")
driver.quit()