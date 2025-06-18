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
# Clicking navigation: Procurement and sourcing
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Procurement and sourcing']")
# Clicking navigation: Purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: All purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Clicking (default) on: PurchOrder
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']")
     Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'HeaderView')]")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedViewEditButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedViewEditButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")
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