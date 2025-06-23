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
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orde']")
# Clicking navigation: Open prepayments
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Open prepayments']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewButton']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='New']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='New']/ancestor::button")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewPaymentJournal']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewPaymentJournal']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Vendor payment journal']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Vendor payment journal']/ancestor::button")
#    "Skipping grid since it is deafault behavior of d365"
# Inputting into: JournalName
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'JournalName')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
            #clicking inside grid: JournalName
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'JournalName')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'JournalName')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'JournalName')])[1]", "VendPay")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "VendPay")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'JournalName')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'JournalName')]", "VendPay")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "VendPay")
        Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Inquiries']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Inquiries']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Inquiries']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Inquiries']/ancestor::button")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='BalanceControl']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='BalanceControl']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Balance control']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Balance control']/ancestor::button")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Close']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Close']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Close']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Close']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='JournalLines']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='JournalLines']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='JournalLines']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='JournalLines']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Lines']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Lines']")
        else:
            Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
            if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='JournalLines']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='JournalLines']")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Lines']")):
                Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Lines']")
#    "Skipping grid since it is deafault behavior of d365"
# Inputting into: LedgerJournalTrans_AccountNum
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
            #clicking inside grid: LedgerJournalTrans_AccountNum
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "checkgrid1")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "checkgrid1")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "checkgrid1")
            else:
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "checkgrid1")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "checkgrid1")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "checkgrid1")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "checkgrid1")
            else:
                actions.move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "checkgrid1")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonPaymProposal']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonPaymProposal']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Payment proposal']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Payment proposal']/ancestor::button")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='VendPaymProposalCreate']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='VendPaymProposalCreate']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Create payment proposal']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Create payment proposal']/ancestor::button")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OkButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OkButton']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CommandButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CommandButton']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")
# Closing the page
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
        time.sleep(1)
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonCheckJournal']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonCheckJournal']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Validate']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Validate']/ancestor::button")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CheckVoucher']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CheckVoucher']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Validate voucher only']/ancestor::button")):
            Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Validate voucher only']/ancestor::button")
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