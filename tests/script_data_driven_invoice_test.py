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
# Clicking navigation: Invoices
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Invoices']")
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
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'CompanyLookup')])[1]", "",base.steps_count,"In the Company field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Company')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Company')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Company')])[1]", "",base.steps_count,"In the Company field, enter or select a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'CompanyLookup')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'CompanyLookup')]", "",base.steps_count,"In the Company field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Company')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Company')]", "",base.steps_count,"In the Company field, enter or select a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
        base.steps_count +=1
#    "Skipping grid selection due input in the ancestor"
        base.steps_count +=1
# Inputting into: PurchParmTable_InvoiceAccount
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_InvoiceAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Invoice account')]") ):
            #clicking inside grid: PurchParmTable_InvoiceAccount
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_InvoiceAccount')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_InvoiceAccount')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_InvoiceAccount')])[1]", "",base.steps_count,"In the Invoice account field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Invoice account')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Invoice account')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Invoice account')])[1]", "",base.steps_count,"In the Invoice account field, enter or select a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_InvoiceAccount')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_InvoiceAccount')]", "",base.steps_count,"In the Invoice account field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Invoice account')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Invoice account')]", "",base.steps_count,"In the Invoice account field, enter or select a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: PurchParmTable_Num
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Number')]") ):
            #clicking inside grid: PurchParmTable_Num
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_Num')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_Num')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_Num')])[1]", "",base.steps_count,"In the Number field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Number')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Number')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Number')])[1]", "",base.steps_count,"In the Number field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]", "",base.steps_count,"In the Number field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Number')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Number')]", "",base.steps_count,"In the Number field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: InvoiceDetails_Description
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InvoiceDetails_Description')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Invoice description')]") ):
            #clicking inside grid: InvoiceDetails_Description
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InvoiceDetails_Description')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InvoiceDetails_Description')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InvoiceDetails_Description')])[1]", "",base.steps_count,"In the Invoice description field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Invoice description')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Invoice description')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Invoice description')])[1]", "",base.steps_count,"In the Invoice description field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InvoiceDetails_Description')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InvoiceDetails_Description')]", "",base.steps_count,"In the Invoice description field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Invoice description')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Invoice description')]", "",base.steps_count,"In the Invoice description field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: PurchParmTable_PurchId
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]") ):
            #clicking inside grid: PurchParmTable_PurchId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchId')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_PurchId')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchId')])[1]", "",base.steps_count,"In the Purchase order field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase order')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Purchase order')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase order')])[1]", "",base.steps_count,"In the Purchase order field, enter or select a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]", "",base.steps_count,"In the Purchase order field, enter or select a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]", "",base.steps_count,"In the Purchase order field, enter or select a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: PurchParmTable_PurchId
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]") ):
            #clicking inside grid: PurchParmTable_PurchId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchId')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_PurchId')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchId')])[1]", "",base.steps_count,"In the Purchase order field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase order')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Purchase order')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase order')])[1]", "",base.steps_count,"In the Purchase order field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchId')]", "",base.steps_count,"In the Purchase order field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase order')]", "",base.steps_count,"In the Purchase order field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: PurchParmTable_PurchAggHeader_PurchNumberSequence
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]") ):
            #clicking inside grid: PurchParmTable_PurchAggHeader_PurchNumberSequence
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')])[1]", "",base.steps_count,"In the Purchase agreement field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase agreement')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase agreement')])[1]", "",base.steps_count,"In the Purchase agreement field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')]", "",base.steps_count,"In the Purchase agreement field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]", "",base.steps_count,"In the Purchase agreement field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# clicking dropdown for Tree
        Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader')]/parent::div/parent::div/following-sibling::div/div",)
        base.steps_count +=1
# Inputting into: PurchParmTable_PurchAggHeader_PurchNumberSequence
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]") ):
            #clicking inside grid: PurchParmTable_PurchAggHeader_PurchNumberSequence
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')])[1]", "",base.steps_count,"In the Purchase agreement field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase agreement')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase agreement')])[1]", "",base.steps_count,"In the Purchase agreement field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_PurchNumberSequence')]", "",base.steps_count,"In the Purchase agreement field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]", "",base.steps_count,"In the Purchase agreement field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# Inputting into: PurchParmTable_PurchAggHeader_CompanyInfo_DataArea
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_CompanyInfo_DataArea')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]") ):
            #clicking inside grid: PurchParmTable_PurchAggHeader_CompanyInfo_DataArea
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchAggHeader_CompanyInfo_DataArea')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_PurchAggHeader_CompanyInfo_DataArea')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_PurchAggHeader_CompanyInfo_DataArea')])[1]", "",base.steps_count,"In the Purchase agreement field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase agreement')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase agreement')])[1]", "",base.steps_count,"In the Purchase agreement field, type a value.")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_CompanyInfo_DataArea')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader_CompanyInfo_DataArea')]", "",base.steps_count,"In the Purchase agreement field, type a value.")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]", "",base.steps_count,"In the Purchase agreement field, type a value.")
        Interactions.press_enter(driver, By.XPATH, "//body")
        base.steps_count +=1
# clicking dropdown for Tree
        Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_PurchAggHeader')]/parent::div/parent::div/following-sibling::div/div",)
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'VendInvoiceInfoTable_ReceivedDate')]")):
            Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Invoice received date')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'VendInvoiceInfoTable_ReceivedDate')]", "06/28/2025",base.steps_count,"In the Invoice received date field, enter a date.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Invoice received date')]")):
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Invoice received date')]", "06/28/2025",base.steps_count,"In the Invoice received date field, enter a date.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_DocumentDate')]")):
            Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Invoice date')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_DocumentDate')]", "06/28/2025",base.steps_count,"In the Invoice date field, enter a date.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Invoice date')]")):
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Invoice date')]", "06/28/2025",base.steps_count,"In the Invoice date field, enter a date.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'VendInvoiceInfoTable_VendorVATDate')]")):
            Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Date of vendor VAT register')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'VendInvoiceInfoTable_VendorVATDate')]", "06/28/2025",base.steps_count,"In the Date of vendor VAT register field, enter a date.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Date of vendor VAT register')]")):
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Date of vendor VAT register')]", "06/28/2025",base.steps_count,"In the Date of vendor VAT register field, enter a date.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_TransDate')]")):
            Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Posting date')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_TransDate')]", "06/28/2025",base.steps_count,"In the Posting date field, enter a date.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Posting date')]")):
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Posting date')]", "06/28/2025",base.steps_count,"In the Posting date field, enter a date.")
        base.steps_count +=1
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_FixedDueDate')]")):
            Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Due date')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_FixedDueDate')]", "06/28/2025",base.steps_count,"In the Due date field, enter a date.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Due date')]")):
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Due date')]", "06/28/2025",base.steps_count,"In the Due date field, enter a date.")
        base.steps_count +=1
# Clicking checkbox: PurchParmTable_Hold
        if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'On hold')]/following-sibling::div/span[1]")):
            Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//label[contains(text(),'On hold')]/following-sibling::div/span[1]", True)
            Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'On hold')]/following-sibling::div/span[1]", base.steps_count,"Select Yes in the On hold field.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'PurchParmTable_Hold') and (@class='toggle-box' or @class='checkBox')]")):
            if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//span[contains(@id, 'PurchParmTable_Hold') and (@class='toggle-box' or @class='checkBox')]", True) == False:
                Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'PurchParmTable_Hold') and (@class='toggle-box' or @class='checkBox')]",base.steps_count,"Select Yes in the On hold field.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@aria-label='On hold']//span")):
            if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//div[@aria-label='On hold']//span", True) == False:
                Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='On hold']//span", base.steps_count,"Select Yes in the On hold field.")
        base.steps_count +=1
# Clicking checkbox: AllowLineQtyChange
        if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Allow matched invoice line quantity deduction')]/following-sibling::div/span[1]")):
            Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//label[contains(text(),'Allow matched invoice line quantity deduction')]/following-sibling::div/span[1]", True)
            Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Allow matched invoice line quantity deduction')]/following-sibling::div/span[1]", base.steps_count,"Select Yes in the Allow matched invoice line quantity deduction field.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'AllowLineQtyChange') and (@class='toggle-box' or @class='checkBox')]")):
            if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//span[contains(@id, 'AllowLineQtyChange') and (@class='toggle-box' or @class='checkBox')]", True) == False:
                Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'AllowLineQtyChange') and (@class='toggle-box' or @class='checkBox')]",base.steps_count,"Select Yes in the Allow matched invoice line quantity deduction field.")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@aria-label='Allow matched invoice line quantity deduction']//span")):
            if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//div[@aria-label='Allow matched invoice line quantity deduction']//span", True) == False:
                Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Allow matched invoice line quantity deduction']//span", base.steps_count,"Select Yes in the Allow matched invoice line quantity deduction field.")
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