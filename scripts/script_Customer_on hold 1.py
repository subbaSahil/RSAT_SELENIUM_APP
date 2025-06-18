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
# Clicking navigation: Accounts receivable
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
# Clicking navigation: Customers
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers']")
# Clicking navigation: Customers on hold
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers on hold']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewCustomer']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewCustomer']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewCustomer']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewCustomer']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='NewCustomer']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='NewCustomer']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='New']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='New']")
# Inputting into: DynamicHeader_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]") ):
          #clicking inside grid: DynamicHeader_AccountNum
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DynamicHeader_AccountNum')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DynamicHeader_AccountNum')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicHeader_AccountNum')])[1]", "US-012")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Customer account')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]", "US-012")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]", "US-012")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]", "US-012")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
# Inputting into: Org_Name
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Org_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
          #clicking inside grid: Org_Name
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Org_Name')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]", "Contoso Retail New York")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "Contoso Retail New York")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Org_Name')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Org_Name')]", "Contoso Retail New York")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "Contoso Retail New York")
     Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OkButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OkButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
# Inputting into: DynamicDetail_CustGroup
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]") ):
          #clicking inside grid: DynamicDetail_CustGroup
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DynamicDetail_CustGroup')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DynamicDetail_CustGroup')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicDetail_CustGroup')])[1]", "40")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer group')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Customer group')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Customer group')])[1]", "40")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]", "40")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]", "40")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
     sucess_save_flag = False
     success_save_flag = Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OKButton']")
     if success_save_flag == False:
         sucess_save_flag = Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CancelButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CancelButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CancelButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CancelButton']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='mibCustPackingSlipJournal']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='mibCustPackingSlipJournal']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='mibCustPackingSlipJournal']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='mibCustPackingSlipJournal']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Packing slips']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Packing slips']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='mibCustPackingSlipJournal']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='mibCustPackingSlipJournal']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Packing slips']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Packing slips']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LedgerTransactVoucher']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LedgerTransactVoucher']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransactVoucher']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransactVoucher']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Vouchers']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Vouchers']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransactVoucher']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransactVoucher']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Vouchers']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Vouchers']")
#    "Skipping grid since it is deafault behavior of d365"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='TransactionLog']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='TransactionLog']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TransactionLog']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TransactionLog']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Audit trail']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Audit trail']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TransactionLog']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TransactionLog']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Audit trail']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Audit trail']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LedgerTransact']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LedgerTransact']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransact']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransact']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Voucher transactions']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Voucher transactions']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransact']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransact']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Voucher transactions']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Voucher transactions']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LedgerTransAccount']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LedgerTransAccount']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransAccount']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransAccount']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Transactions']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Transactions']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransAccount']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransAccount']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Transactions']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Transactions']")
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LedgerTransSettled']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LedgerTransSettled']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransSettled']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransSettled']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Ledger settlements']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Ledger settlements']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransSettled']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransSettled']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Ledger settlements']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Ledger settlements']")
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LedgerTransVoucher']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LedgerTransVoucher']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransVoucher']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransVoucher']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Voucher']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Voucher']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransVoucher']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='LedgerTransVoucher']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Voucher']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Voucher']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='EditVoucher']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='EditVoucher']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Edit voucher']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Edit voucher']/ancestor::button")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LedgerVoucherTransAuditLog']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LedgerVoucherTransAuditLog']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Audit trail of voucher edits']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Audit trail of voucher edits']/ancestor::button")
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
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='TaxTransactions']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='TaxTransactions']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TaxTransactions']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TaxTransactions']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Posted sales tax']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Posted sales tax']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TaxTransactions']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TaxTransactions']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Posted sales tax']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Posted sales tax']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Cov']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Cov']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Cov']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Cov']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Cash flow forecasts']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Cash flow forecasts']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='Cov']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='Cov']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Cash flow forecasts']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Cash flow forecasts']")
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='TaxTransactions']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='TaxTransactions']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TaxTransactions']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TaxTransactions']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Posted sales tax']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Posted sales tax']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TaxTransactions']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='TaxTransactions']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Posted sales tax']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Posted sales tax']")
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