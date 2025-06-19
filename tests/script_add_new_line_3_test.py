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
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Vendors
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors']")
# Clicking navigation: All vendors
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All vendors']")
# Closing the page
        Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
        time.sleep(1)
        Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Purchase orders
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: All purchase orders
        Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
        user_input = input("Press data to select: ")
        Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
        Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LineStripNew']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LineStripNew']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")
        count = Interactions.check_for_line_item_count(driver, By.XPATH, "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]")
        row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']",count)
#    "Skipping grid since it is deafault behavior of d365"
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
        #clicking inside grid: PurchLine_ItemId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")):
                actions.move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "P0004")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "P0004")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]") ):
            #clicking inside grid: PurchLine_PurchReceivedNow
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")):
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")).perform()
                Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]", "1.00")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")):
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")).perform()
                Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]", "1.00")
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
        if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LineStripNew']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LineStripNew']")
        elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")):
            Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")
        count = Interactions.check_for_line_item_count(driver, By.XPATH, "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]")
        row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']",count)
#    "Skipping grid since it is deafault behavior of d365"
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
        #clicking inside grid: PurchLine_ItemId
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")):
                actions.move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "M0056")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "M0056")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
        if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]") ):
            #clicking inside grid: PurchLine_PurchReceivedNow
            if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")):
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")).perform()
                Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]", "2.00")
            elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")):
                actions.move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")).perform()
                Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]", "2.00")
        Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
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