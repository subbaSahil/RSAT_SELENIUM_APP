import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base import BaseTest
from selenium.webdriver.common.by import By
import Interactions
import time
base = BaseTest()
driver = base.driver
actions = base.actions
test_passed = base.test_passed
def test():
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
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00001254")
            Interactions.press_enter(driver, By.XPATH, locator)
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00001254")
            Interactions.press_enter(driver, By.XPATH, locator)
# Clicking button: Grid
        if Interactions.check_element_exist(driver, By.XPATH, f"//input[@value='00001254']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']"):
             Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='00001254']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
        else:
             Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='00001254']")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='00001254']")
        assert True
    except Exception as e:
        test_passed = False
        raise e
    finally:
        if test_passed:
            print("✅ Test case passed")
            Interactions.take_screenshot_on_pass(driver, "test_case_passed")
        else:
            print("❌ Test case failed")
            Interactions.take_screenshot_on_failure(driver, "test_case_failed")
        driver.quit()