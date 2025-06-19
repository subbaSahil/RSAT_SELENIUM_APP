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