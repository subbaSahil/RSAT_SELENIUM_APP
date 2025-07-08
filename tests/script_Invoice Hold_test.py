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
        # Clicking navigation: Procurement and sourcing
        nav1 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Procurement and sourcing']")
        # Clicking navigation: Vendors
        nav2 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Vendors']")
        # Clicking navigation: All vendors
        base.steps_count +=1
        nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='All vendors']",base.steps_count, "Go to Procurement and sourcing > Vendors > All vendors.")
        time.sleep(3)
        Interactions.assert_navigation(driver,nav1, "Vend", nav3)
#         base.steps_count +=1
#         user_input = input("Press data to select: ")
#         Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']", base.steps_count,"In the list, find and select the desired record.")
#         base.steps_count +=1
#         Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
#         base.steps_count +=1
# # Clicking (default) on: VendorTab
#         time.sleep(3)
#         Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='VendorTab']",base.steps_count,"On the Action Pane, click Vendor.")
#         base.steps_count +=1
#         if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OnHoldDropDialogButton']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OnHoldDropDialogButton']",base.steps_count,"Click On hold to open the drop dialog.")
#         elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OnHoldDropDialogButton']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OnHoldDropDialogButton']",base.steps_count,"Click On hold to open the drop dialog.")
#         elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='On hold']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='On hold']",base.steps_count,"Click On hold to open the drop dialog.")
#         else:
#             Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
#             if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='OnHoldDropDialogButton']")):
#                 Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='OnHoldDropDialogButton']",base.steps_count,"Click On hold to open the drop dialog.")
#             elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='On hold']")):
#                 Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='On hold']",base.steps_count,"Click On hold to open the drop dialog.")
#         base.steps_count +=1
# # Clicking combobox: OnHold
#         combox_box_to_click = None
#         if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='OnHold']/following-sibling::div"):
#             combox_box_to_click = "//input[@name='OnHold']/following-sibling::div"
#         elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Vendor hold']/following-sibling::div"):
#             combox_box_to_click = "//input[@aria-label='Vendor hold']/following-sibling::div"
#         elif Interactions.check_element_exist(driver, By.XPATH, "//input[@name='OnHold']/parent::div/following-sibling::div/div"):
#             combox_box_to_click = "//input[@name='OnHold']/parent::div/following-sibling::div/div"
#         Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
#         if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]//li[@data-dyn-index='1']"):
#             Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]//li[@data-dyn-index='1']", base.steps_count,"In the Vendor hold field, select an option.")
#         elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'OnHold')]//li[1]"):
#             Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'OnHold')]//li[1]",base.steps_count,"In the Vendor hold field, select an option.")
#         else:
#             if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]"):
#                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'OnHold')]",By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]//li[@data-dyn-index='1']", base.steps_count,"In the Vendor hold field, select an option.")
#                 if cliked_or_not == False:
#                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'OnHold')]",By.XPATH, "//ul[contains(@id,'OnHold')]//li[1]", base.steps_count)
#             elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'OnHold')]"):
#                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'OnHold')]",By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]//li[@data-dyn-index='1']",base.steps_count,"In the Vendor hold field, select an option.")
#                 if cliked_or_not == False:
#                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'OnHold')]",By.XPATH, "//ul[contains(@id,'OnHold')]//li[1]", base.steps_count,"In the Vendor hold field, select an option.")
#         base.steps_count +=1
# # Inputting into: ReasonCode
#         if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'ReasonCode')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Reason code')]") ):
#             #clicking inside grid: ReasonCode
#             if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'ReasonCode')])[1]")):
#                 actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'ReasonCode')]")).perform()
#                 Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'ReasonCode')])[1]", "",base.steps_count,"In the Reason code field, enter or select a value.")
#             elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Reason code')])[1]")):
#                 actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Reason code')]")).perform()
#                 Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Reason code')])[1]", "",base.steps_count,"In the Reason code field, enter or select a value.")
#         else:
#             if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ReasonCode')]")):
#                 Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'ReasonCode')]", "",base.steps_count,"In the Reason code field, enter or select a value.")
#             elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Reason code')]")):
#                 Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Reason code')]", "",base.steps_count,"In the Reason code field, enter or select a value.")
#         Interactions.press_enter(driver, By.XPATH, "//body")
#         base.steps_count +=1
# # Clicking button: Grid
#         user_input = input("Press data to select: ")
#         Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']", base.steps_count,"In the list, select row 4.")
#         Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
#         base.steps_count +=1
# #    "Skipping grid selection due input in the ancestor"
#         base.steps_count +=1
#         if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CommandButtonOK']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CommandButtonOK']",base.steps_count, "Click OK.")
#         elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButtonOK']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButtonOK']",base.steps_count,"Click OK.")
# # Clicking the form caption
#         Interactions.wait_and_click(driver, By.XPATH, "//span[@class='formCaption link-content-validLink']")
# # Closing the page
#         base.steps_count +=1
#         Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']", base.steps_count)
#         time.sleep(1)
#         Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# # Clicking navigation: Procurement and sourcing
#         nav1 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Procurement and sourcing']")
# # Clicking navigation: Purchase orders
#         nav2 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# # Clicking navigation: All purchase orders
#         base.steps_count +=1
#         nav3 = Interactions.click_nav(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']",base.steps_count, "Go to Procurement and sourcing > Purchase orders > All purchase orders.")
#         time.sleep(3)
#         Interactions.assert_navigation(driver,nav1, nav2, nav3)
#         base.steps_count +=1
#         if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']",base.steps_count, "Click New.")
#         elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']",base.steps_count,"Click New.")
#         base.steps_count +=1
# # Inputting into: PurchTable_OrderAccount
#         if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]") ):
#             #clicking inside grid: PurchTable_OrderAccount
#             if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]")):
#                 actions.move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_OrderAccount')]")).perform()
#                 Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]", "",base.steps_count,"In the Vendor account field, enter or select a value.")
#             elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]")):
#                 actions.move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Vendor account')]")).perform()
#                 Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]", "",base.steps_count,"In the Vendor account field, enter or select a value.")
#         else:
#             if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
#                 Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "",base.steps_count,"In the Vendor account field, enter or select a value.")
#             elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
#                 Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "",base.steps_count,"In the Vendor account field, enter or select a value.")
#         Interactions.press_enter(driver, By.XPATH, "//body")
#         base.steps_count +=1
# # Clicking button: Grid
#         user_input = input("Press data to select: ")
#         Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']", base.steps_count,"In the list, select row 10.")
#         Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
#         base.steps_count +=1
# #    "Skipping grid selection due input in the ancestor"
#         base.steps_count +=1
#         if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']",base.steps_count, "Click OK.")
#         elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
#             Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']",base.steps_count,"Click OK.")
#         base.steps_count +=1
#         base.steps_count +=1
#         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']",base.steps_count, "Click Save.")
# # Clicking the form caption
#         Interactions.wait_and_click(driver, By.XPATH, "//span[@class='formCaption link-content-validLink']")
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