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
# Clicking (default) on: PurchOrder
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Totals']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Totals']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Totals']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Totals']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Totals']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Totals']")
        else:
            Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
            if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='Totals']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='Totals']")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Totals']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Totals']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OKButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OKButton']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
# Clicking (default) on: Purchase
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Purchase']")
# Clicking (default) on: Manage
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Manage']")
# Clicking (default) on: Invoice
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Invoice']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='VendOpenTrans']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='VendOpenTrans']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='VendOpenTrans']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='VendOpenTrans']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Open transactions']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Open transactions']")
        else:
            Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
            if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='VendOpenTrans']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='VendOpenTrans']")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Open transactions']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Open transactions']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Save']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Save']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Save']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Save']")
# Clicking (default) on: Retail
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Retail']")
# Clicking (default) on: WHS
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='WHS']")
# Clicking (default) on: TMS
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='TMS']")
# Clicking (default) on: General
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='General']")
# Clicking (default) on: SystemDefinedOptions
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='SystemDefinedOptions']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedShowMenuButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedShowMenuButton']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Go to']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Go to']/ancestor::button")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedHeaderDetailsViewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedHeaderDetailsViewButton']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Header']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Header']/ancestor::button")
# Clicking (default) on: PurchOrder
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']")
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