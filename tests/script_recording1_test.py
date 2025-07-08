import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.base import BaseTest
from selenium.webdriver.common.by import By
from Utils import Interactions
from Utils.screenRecorder import ScreenRecorder
import time
@pytest.mark.ui
 
def test():
    base = BaseTest("user1",incognito=True)
    driver = base.driver
    actions = base.actions
    recorder=ScreenRecorder()
    try:
        recorder.start()
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
        nav1 = Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Invoices
        nav2 = Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Invoices']")
        # time.sleep(3)
        # Interactions.assert_navigation(driver,nav1,nav2)
# Clicking navigation: Pending vendor invoices
        base.steps_count +=1
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Pending vendor invoices']",base.steps_count, "Go to Accounts payable > Invoices > Pending vendor invoices.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewInvoice']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewInvoice']",base.steps_count,"Click New.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewInvoice']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewInvoice']",base.steps_count,"Click New.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']",base.steps_count,"Click New.")
        else:
            Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
            if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='NewInvoice']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='NewInvoice']",base.steps_count,"Click New.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='New']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='New']",base.steps_count,"Click New.")
        base.steps_count +=1
# Inputting into: CompanyLookup
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'CompanyLookup')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Company')]") ):
            #clicking inside grid: CompanyLookup
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'CompanyLookup')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'CompanyLookup')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'CompanyLookup')])[1]", "GLOC",base.steps_count,"In the Company field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Company')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Company')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Company')])[1]", "GLOC",base.steps_count,"In the Company field, enter or select a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'CompanyLookup')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'CompanyLookup')]", "GLOC",base.steps_count,"In the Company field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Company')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Company')]", "GLOC",base.steps_count,"In the Company field, enter or select a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: PurchParmTable_InvoiceAccount
       
        assert True
    except Exception as e:
        base.test_passed = False
        raise e
    finally:
        Interactions.log_interaction(" ", " ", " "," ")
        if base.test_passed:
            print("✅ Test case passed")
            Interactions.take_screenshot_on_pass(driver)
            recorder.stop_and_save()
        else:
            print("❌ Test case failed")
            Interactions.take_screenshot_on_failure(driver)
            recorder.stop_and_discard()
        driver.quit()
 