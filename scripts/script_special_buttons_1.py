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
# Clicking navigation: Purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: All purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SysPAMenuButton']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SysPAMenuButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Power Apps']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Power Apps']/ancestor::button")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SysPAMenuButton_SysPAAddNew']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SysPAMenuButton_SysPAAddNew']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Add an app']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Add an app']/ancestor::button")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Cancel']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Cancel']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Cancel']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Cancel']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedOfficeButton']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedOfficeButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Open in Microsoft Office']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Open in Microsoft Office']/ancestor::button")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedOfficeButton_Default_PurchApprovalHeaderEntity']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedOfficeButton_Default_PurchApprovalHeaderEntity']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Purchase order for approval (unfiltered)']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Purchase order for approval (unfiltered)']/ancestor::button")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='DownloadButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='DownloadButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='DownloadButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='DownloadButton']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedAttachButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedAttachButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedAttachButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedAttachButton']")
# Refreshing the page
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedRefreshButton']")
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