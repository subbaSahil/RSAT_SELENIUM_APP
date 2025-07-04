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
# Clicking navigation: Accounts receivable
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
# Clicking navigation: Customers
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers']")
# Clicking navigation: All customers
        base.steps_count +=1
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All customers']",base.steps_count, "Go to Accounts receivable > Customers > All customers.")
# Inputting into: QuickFilterControl
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "200",base.steps_count,"Use the Quick Filter to find records. For example, filter on the Name field with a value of '200'.")
            Interactions.press_enter(driver, By.XPATH, locator)
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "200",base.steps_count,"Use the Quick Filter to find records. For example, filter on the Name field with a value of '200'.")
            Interactions.press_enter(driver, By.XPATH, locator)
        base.steps_count +=1
# Clicking button: Grid
        if Interactions.check_element_exist(driver, By.XPATH, f"//input[@value='200']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']"):
             Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='200']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']", base.steps_count,"In the list, click the link in the selected row.")
        else:
             Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='200']", base.steps_count,"In the list, click the link in the selected row.")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='200']")
        base.steps_count +=1
# Clicking (default) on: aptabSell
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='aptabSell']",base.steps_count,"On the Action Pane, click Sell.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedViewEditButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedViewEditButton']",base.steps_count, "Click Edit.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']",base.steps_count,"Click Edit.")
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