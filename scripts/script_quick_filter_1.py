import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base import BaseTest
from selenium.webdriver.common.by import By
import Interactions
import time
base = BaseTest()
driver = base.driver
ActionChains = base.ActionChains
test_passed = base.test_passed
try:
     Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: All purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
# Inputting into: GridFilter
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00001")
         Interactions.press_enter(driver, By.XPATH, locator)
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00001")
         Interactions.press_enter(driver, By.XPATH, locator)
# Clicking (default) on: Purchase
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Purchase']")
# Clicking (default) on: PurchOrder
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']")
# Inputting into: GridFilter
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00000")
         Interactions.press_enter(driver, By.XPATH, locator)
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00000")
         Interactions.press_enter(driver, By.XPATH, locator)
# Inputting into: GridFilter
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00000859")
         Interactions.press_enter(driver, By.XPATH, locator)
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00000859")
         Interactions.press_enter(driver, By.XPATH, locator)
# Clicking button: Grid
     if Interactions.check_element_exist(driver, By.XPATH, f"//input[@value='00000859']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']"):
          Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='00000859']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='00000859']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='00000859']")
# Clicking (default) on: PurchOrder
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']")
# Inputting into: GridFilter
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "000008")
         Interactions.press_enter(driver, By.XPATH, locator)
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "000008")
         Interactions.press_enter(driver, By.XPATH, locator)
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Clicking (default) on: PurchOrder
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']")
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