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
# Clicking navigation: Accounts payable
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: Purchase orders assigned to me
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders assigned to me']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
# Inputting into: PurchTable_OrderAccount
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]") ):
          #clicking inside grid: PurchTable_OrderAccount
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_OrderAccount')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]", "1003")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Vendor account')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]", "1003")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "1003")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "1003")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Clicking (default) on: PurchOrder
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']")
#    "Skipping grid since it is deafault behavior of d365"
# Inputting into: PurchLine_ItemId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
          #clicking inside grid: PurchLine_ItemId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_ItemId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid"
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
# Inputting into: PurchLine_ItemId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
          #clicking inside grid: PurchLine_ItemId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_ItemId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]", "C0001")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "C0001")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "C0001")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "C0001")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: PurchLine_ItemId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
          #clicking inside grid: PurchLine_ItemId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_ItemId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
#    "Skipping grid selection due input in the ancestor"
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
# Clicking (default) on: Purchase
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Purchase']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonConfirm']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonConfirm']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='buttonConfirm']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='buttonConfirm']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Confirm']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Confirm']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='buttonConfirm']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='buttonConfirm']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Confirm']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Confirm']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Ok']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Ok']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Ok']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Ok']")
# Clicking (default) on: Receive
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Receive']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonUpdatePackingSlip']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonUpdatePackingSlip']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='buttonUpdatePackingSlip']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='buttonUpdatePackingSlip']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Product receipt']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Product receipt']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='buttonUpdatePackingSlip']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='buttonUpdatePackingSlip']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Product receipt']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Product receipt']")
# Inputting into: PurchParmTable_Num
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Product receipt')]") ):
          #clicking inside grid: PurchParmTable_Num
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_Num')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_Num')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_Num')])[1]", "PR-66")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Product receipt')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Product receipt')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Product receipt')])[1]", "PR-66")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]", "PR-66")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Product receipt')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Product receipt')]", "PR-66")
     Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Clicking (default) on: Invoice
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Invoice']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonUpdateInvoice']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonUpdateInvoice']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='buttonUpdateInvoice']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='buttonUpdateInvoice']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Invoice']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Invoice']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='buttonUpdateInvoice']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='buttonUpdateInvoice']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Invoice']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Invoice']")
# Inputting into: PurchParmTable_Num
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Number')]") ):
          #clicking inside grid: PurchParmTable_Num
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_Num')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchParmTable_Num')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchParmTable_Num')])[1]", "INV-900000")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Number')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Number')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Number')])[1]", "INV-900000")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]", "INV-900000")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Number')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Number')]", "INV-900000")
     Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='UpdateMatchStatus']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='UpdateMatchStatus']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='UpdateMatchStatus']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='UpdateMatchStatus']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
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