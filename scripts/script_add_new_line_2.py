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
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "A0001")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "A0001")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
         #clicking inside grid: PurchLine_ItemId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "")
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
         #clicking inside grid: PurchLine_ItemId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "")
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
         #clicking inside grid: PurchLine_ItemId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "")
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
         #clicking inside grid: PurchLine_ItemId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
         #clicking inside grid: PurchLine_ItemId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
         #clicking inside grid: InventoryDimensionsGrid_InventLocationId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')])[" + row_number + "]", "18")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[" + row_number + "]", "18")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]") ):
          #clicking inside grid: PurchLine_PurchReceivedNow
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")):
                 ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")).perform()
                 Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]", "12.00")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")):
                 ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")).perform()
                 Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]", "12.00")
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
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "D0006")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "D0006")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]") ):
          #clicking inside grid: PurchLine_PurchReceivedNow
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")):
                 ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")).perform()
                 Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]", "100.00")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")):
                 ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")).perform()
                 Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]", "100.00")
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
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
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[" + row_number + "]", "D0013")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[" + row_number + "]", "D0013")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]") ):
          #clicking inside grid: PurchLine_PurchReceivedNow
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")):
                 ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]")).perform()
                 Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[" + row_number + "]", "99.00")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")):
                 ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]")).perform()
                 Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[" + row_number + "]", "99.00")
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
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