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

save_line_items_without_errors = False

test_passed = True

try:
     Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Broker and royalties
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Broker and royalties']")
# Clicking navigation: Broker claims
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Broker claims']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SSRS_OpenBrokerInvoices']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SSRS_OpenBrokerInvoices']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SSRS_OpenBrokerInvoices']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SSRS_OpenBrokerInvoices']")
# Open dropdown for Broker
     Interactions.wait_and_click(driver, By.XPATH, "//input[@name='Fld1_1']/following-sibling::div//*[contains(@class, 'lookupButton')]")
     container = "//input[@name='Fld1_1']/following-sibling::div//*[contains(@class, 'lookupButton')]/ancestor::div[@id='mainContainer']/following-sibling::div[@data-dyn-role='Popup']//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']"
#    "Skipping grid selection due input in the ancestor"
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CommandButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CommandButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")
except Exception as e:
     test_passed = False
     print("Test case failed:"+ e)
finally:
     if test_passed:
          print("✅ Test case passed")
          Interactions.take_screenshot_on_pass(driver, "test_case_passed")
     else:
          print("❌ Test case failed")
          Interactions.take_screenshot_on_failure(driver, "test_case_failed")
     driver.quit()