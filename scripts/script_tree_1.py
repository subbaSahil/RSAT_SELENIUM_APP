from base import BaseTest
from selenium.webdriver.common.by import By
import Interactions
import time
base = BaseTest()
driver = base.driver
ActionChains = base.ActionChains
test_passed = base.test_passed
try:
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