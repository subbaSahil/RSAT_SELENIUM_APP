import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base import BaseTest
from selenium.webdriver.common.by import By
import Interactions
import time
@pytest.mark.ui
def test():
    base = BaseTest()
    driver = base.driver
    actions = base.actions
    try:
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts receivable
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
# Clicking navigation: Customers
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers']")
# Clicking navigation: All customers
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All customers']")
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
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DynamicHeader_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicHeader_AccountNum')])[1]", "")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Customer account')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]", "")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]", "")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]", "")
        Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: DynamicHeader_AccountNum
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]") ):
            #clicking inside grid: DynamicHeader_AccountNum
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DynamicHeader_AccountNum')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DynamicHeader_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicHeader_AccountNum')])[1]", "RVN")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Customer account')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]", "RVN")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]", "RVN")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]", "RVN")
        Interactions.press_enter(driver, By.XPATH, "//body")
# Closing the page
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
        time.sleep(1)
# Inputting into: Org_Name
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Org_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
            #clicking inside grid: Org_Name
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Org_Name')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]", "")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Org_Name')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Org_Name')]", "")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "")
        Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: Org_Name
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Org_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
            #clicking inside grid: Org_Name
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Org_Name')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]", "4900")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "4900")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Org_Name')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Org_Name')]", "4900")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "4900")
        Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: DynamicDetail_CustGroup
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]") ):
            #clicking inside grid: DynamicDetail_CustGroup
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DynamicDetail_CustGroup')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DynamicDetail_CustGroup')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicDetail_CustGroup')])[1]", "100")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer group')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Customer group')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Customer group')])[1]", "100")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]", "100")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]", "100")
        Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
        sucess_save_flag = False
        success_save_flag = Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OKButton']")
        if success_save_flag == False:
            sucess_save_flag = Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Clicking (default) on: aptabGeneral
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='aptabGeneral']")
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
# Clicking (default) on: aptabCustomer
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='aptabCustomer']")
# Closing the page
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
        time.sleep(1)
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts receivable
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
# Clicking navigation: Customers
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers']")
# Clicking navigation: All customers
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All customers']")
# Inputting into: QuickFilterControl
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "4900")
            Interactions.press_enter(driver, By.XPATH, locator)
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "4900")
            Interactions.press_enter(driver, By.XPATH, locator)
# Inputting into: QuickFilterControl
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "49000")
            Interactions.press_enter(driver, By.XPATH, locator)
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "49000")
            Interactions.press_enter(driver, By.XPATH, locator)
# Inputting into: QuickFilterControl
        if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "4900")
            Interactions.press_enter(driver, By.XPATH, locator)
        elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
            locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
            Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "4900")
            Interactions.press_enter(driver, By.XPATH, locator)
# Clicking button: Grid
        if Interactions.check_element_exist(driver, By.XPATH, f"//input[@value='4900']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']"):
             Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='4900']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
        else:
             Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='4900']")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='4900']")
# Clicking (default) on: aptabGeneral
        time.sleep(3)
        Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='aptabGeneral']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedViewEditButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedViewEditButton']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewContactInfo']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewContactInfo']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewContactInfo']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewContactInfo']")
# Inputting into: ContactInfo_Description
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'ContactInfo_Description')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Description')]") ):
            #clicking inside grid: ContactInfo_Description
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'ContactInfo_Description')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'ContactInfo_Description')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'ContactInfo_Description')])[1]", "adfgh")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Description')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]", "adfgh")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ContactInfo_Description')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'ContactInfo_Description')]", "adfgh")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Description')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Description')]", "adfgh")
        Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: GovernmentIdentification_PartyState
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'GovernmentIdentification_PartyState')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'State')]") ):
            #clicking inside grid: GovernmentIdentification_PartyState
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'GovernmentIdentification_PartyState')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'GovernmentIdentification_PartyState')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'GovernmentIdentification_PartyState')])[1]", "")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'State')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'State')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'State')])[1]", "")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GovernmentIdentification_PartyState')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'GovernmentIdentification_PartyState')]", "")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'State')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'State')]", "")
        Interactions.press_enter(driver, By.XPATH, "//body")
# Closing the page
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
        time.sleep(1)
# Inputting into: CustTable_SegmentId
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'CustTable_SegmentId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Segment')]") ):
            #clicking inside grid: CustTable_SegmentId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'CustTable_SegmentId')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'CustTable_SegmentId')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'CustTable_SegmentId')])[1]", "")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Segment')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Segment')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Segment')])[1]", "")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'CustTable_SegmentId')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'CustTable_SegmentId')]", "")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Segment')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Segment')]", "")
        Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking button: Grid
        user_input = input("Press data to select: ")
        Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Inputting into: SalesGroup
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'SalesGroup')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Sales group')]") ):
            #clicking inside grid: SalesGroup
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'SalesGroup')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'SalesGroup')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'SalesGroup')])[1]", "01")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Sales group')])[1]")):
                actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Sales group')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Sales group')])[1]", "01")
        else:
            if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SalesGroup')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'SalesGroup')]", "01")
            elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Sales group')]")):
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Sales group')]", "01")
        Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='DeleteButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='DeleteButton']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='DeleteButton']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='DeleteButton']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Yes']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Yes']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")
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
 
 