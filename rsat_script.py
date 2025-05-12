from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

import login
import Interactions
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

login.login(driver)

locator = ""

filter_manager_cloumn_last_opened = ""
filter_manager_dropdown_item_index = 1

column_to_open = ""
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
time.sleep(1)
# Clicking navigation: Invoices
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Invoices']")
time.sleep(1)
# Clicking navigation: Invoice journal
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Invoice journal']")
time.sleep(1)
# ❌ Locator not found for: No Control Name (Type: )
# Clicking (default) on: GridOverview
Interactions.wait_and_click(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/div[@aria-rowindex='3']")
# Clicking (default) on: Validation
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Validation']")
# Clicking (default) on: CheckJournal
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CheckJournal']")
# Clicking (default) on: PostJournal
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='PostJournal']")
# Clicking (default) on: LedgerJournalPostTransfer
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LedgerJournalPostTransfer']")
# Clicking (default) on: PrintMenu
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='PrintMenu']")
# Clicking (default) on: LedgerTransPerJournal
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LedgerTransPerJournal']")
# Clicking button: CommandButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")
time.sleep(5)
print("test case passed")
driver.quit()