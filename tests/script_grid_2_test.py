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
def test():
    try:
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
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
# Closing the page
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
        time.sleep(1)
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Vendors
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors']")
# Clicking navigation: All vendors
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All vendors']")
        user_input = input("Press data to select: ")
        Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Clicking (default) on: VendorTab
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='VendorTab']")
# Closing the page
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
        time.sleep(1)
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts receivable
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
# Clicking navigation: Customers
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers']")
# Clicking navigation: All customers
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All customers']")
        user_input = input("Press data to select: ")
        Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Clicking (default) on: aptabProjects
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='aptabProjects']")
        assert True
    except Exception as e:
        base.test_passed = False
        raise e
    finally:
        if base.test_passed:
            print("✅ Test case passed")
            Interactions.take_screenshot_on_pass(driver)
        else:
            print("❌ Test case failed")
            Interactions.take_screenshot_on_failure(driver)
        driver.quit()