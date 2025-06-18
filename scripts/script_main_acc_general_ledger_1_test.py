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
# Clicking navigation: General ledger
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='General ledger']")
# Clicking navigation: Chart of accounts
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Chart of accounts']")
# Clicking navigation: Accounts
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts']")
# Clicking navigation: Main account categories
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Main account categories']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
# Clicking combobox: LedgerAccountCategory_AccountType
     combox_box_to_click = None
     if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"):
          combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Main account type']/following-sibling::div"):
          combox_box_to_click = "//input[@aria-label='Main account type']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"):
          combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"
     Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='2']"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='2']")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[2]"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[2]")
     else:
          if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='2']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[2]")
          elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='2']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[2]")
# Clicking combobox: LedgerAccountCategory_AccountType
     combox_box_to_click = None
     if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"):
          combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Main account type']/following-sibling::div"):
          combox_box_to_click = "//input[@aria-label='Main account type']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"):
          combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"
     Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='3']"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='3']")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[3]"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[3]")
     else:
          if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='3']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[3]")
          elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='3']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[3]")
# Clicking combobox: LedgerAccountCategory_AccountType
     combox_box_to_click = None
     if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"):
          combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Main account type']/following-sibling::div"):
          combox_box_to_click = "//input[@aria-label='Main account type']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"):
          combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"
     Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='4']"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='4']")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[4]"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[4]")
     else:
          if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='4']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[4]")
          elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='4']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[4]")
# Clicking combobox: LedgerAccountCategory_AccountType
     combox_box_to_click = None
     if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"):
          combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Main account type']/following-sibling::div"):
          combox_box_to_click = "//input[@aria-label='Main account type']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"):
          combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"
     Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='5']"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='5']")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[5]"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[5]")
     else:
          if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='5']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[5]")
          elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='5']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[5]")
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