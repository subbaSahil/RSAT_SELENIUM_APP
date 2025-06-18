# Customer_on hold 1.xml
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
user_input = None

save_line_items_without_errors = False

test_passed = True

try:
     Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts receivable
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
# Clicking navigation: Customers
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers']")
# Clicking navigation: Customers on hold
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers on hold']")
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='NewCustomer']", "//button[@data-dyn-controlname='NewCustomer']", "//button[@aria-label='New']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='NewCustomer']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='New']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='NewCustomer']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='New']"])
     Interactions.send_keys_with_multiple_xpaths(driver, By.XPATH,["//input[contains(@name,'DynamicHeader_AccountNum')]", "//input[contains(@aria-label,'Customer account')]"], "US-012")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
     Interactions.send_keys_with_multiple_xpaths(driver, By.XPATH,["//input[contains(@name,'Org_Name')]", "//input[contains(@aria-label,'Name')]"], "Contoso Retail New York")
     Interactions.press_enter(driver, By.XPATH, "//body")
     Interactions.click_multiple_xpaths(driver, By.XPATH, ["//button[@name='OkButton']", "//button[@data-dyn-controlname='OkButton']", "//button[@aria-label='Select']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='OkButton']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Select']"])
     Interactions.send_keys_with_multiple_xpaths(driver, By.XPATH,["//input[contains(@name,'DynamicDetail_CustGroup')]", "//input[contains(@aria-label,'Customer group')]"], "40")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
     sucess_save_flag = False
     success_save_flag = Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OKButton']")
     if success_save_flag == False:
         sucess_save_flag = Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
     Interactions.click_multiple_xpaths(driver, By.XPATH, ["//button[@name='CancelButton']", "//button[@data-dyn-controlname='CancelButton']", "//button[@aria-label='Cancel']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='CancelButton']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Cancel']"])
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='mibCustPackingSlipJournal']", "//button[@data-dyn-controlname='mibCustPackingSlipJournal']", "//button[@aria-label='Packing slips']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='mibCustPackingSlipJournal']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Packing slips']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='mibCustPackingSlipJournal']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Packing slips']"])
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='LedgerTransactVoucher']", "//button[@data-dyn-controlname='LedgerTransactVoucher']", "//button[@aria-label='Vouchers']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransactVoucher']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Vouchers']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransactVoucher']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Vouchers']"])
#    "Skipping grid since it is deafault behavior of d365"
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='TransactionLog']", "//button[@data-dyn-controlname='TransactionLog']", "//button[@aria-label='Audit trail']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TransactionLog']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Audit trail']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TransactionLog']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Audit trail']"])
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='LedgerTransact']", "//button[@data-dyn-controlname='LedgerTransact']", "//button[@aria-label='Voucher transactions']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransact']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Voucher transactions']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransact']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Voucher transactions']"])
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='LedgerTransAccount']", "//button[@data-dyn-controlname='LedgerTransAccount']", "//button[@aria-label='Transactions']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransAccount']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Transactions']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransAccount']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Transactions']"])
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='LedgerTransSettled']", "//button[@data-dyn-controlname='LedgerTransSettled']", "//button[@aria-label='Ledger settlements']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransSettled']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Ledger settlements']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransSettled']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Ledger settlements']"])
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='LedgerTransVoucher']", "//button[@data-dyn-controlname='LedgerTransVoucher']", "//button[@aria-label='Voucher']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransVoucher']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Voucher']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransVoucher']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Voucher']"])
     Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='EditVoucher']", "//span[text()='Edit voucher']/ancestor::button"])
     Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='LedgerVoucherTransAuditLog']", "//span[text()='Audit trail of voucher edits']/ancestor::button"])
# Clicking (default) on: SystemDefinedOptions
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='SystemDefinedOptions']")
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='TaxTransactions']", "//button[@data-dyn-controlname='TaxTransactions']", "//button[@aria-label='Posted sales tax']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TaxTransactions']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Posted sales tax']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TaxTransactions']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Posted sales tax']"])
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='Cov']", "//button[@data-dyn-controlname='Cov']", "//button[@aria-label='Cash flow forecasts']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='Cov']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Cash flow forecasts']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='Cov']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Cash flow forecasts']"])
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     if Interactions.click_multiple_xpaths(driver,By.XPATH,["//button[@name='TaxTransactions']", "//button[@data-dyn-controlname='TaxTransactions']", "//button[@aria-label='Posted sales tax']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TaxTransactions']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Posted sales tax']"]):
          pass
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          Interactions.click_multiple_xpaths(driver, By.XPATH, ["//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TaxTransactions']", "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Posted sales tax']"])
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
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

