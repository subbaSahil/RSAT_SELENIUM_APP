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
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Purchase orders
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: Open prepayments
        base.steps_count +=1
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Open prepayments']",base.steps_count, "Go to Accounts payable > Purchase orders > Open prepayments.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewButton']", base.steps_count,"Click New.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='New']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='New']/ancestor::button",base.steps_count,"Click New.")
        base.steps_count +=1
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