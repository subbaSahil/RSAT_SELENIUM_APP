from base import BaseTest
from selenium.webdriver.common.by import By
import Interactions

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
# Clicking filter manager: SystemDefinedFilterManager
     column_to_open = "Purchase order status"
     open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
     filter_manager_cloumn_last_opened = ''
     for i, div in enumerate(open_divs, start=1):
         class_attr = div.get_attribute('class')
         if 'hasOpenPopup' in class_attr:
              filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[1]")
              break
     if filter_manager_cloumn_last_opened == 'Purchase order status' and filter_manager_cloumn_last_opened != '':
         Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order status']")
         Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order status']")
     else:
         Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order status']")
     filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of 'Received' on the 'Purchase order status' field using the 'is exactly' filter operator.")
     operator = filter_manager_data['operator']
     new_val = filter_manager_data['value']
     field_name = filter_manager_data['field_name']
     drop_down_item = "//input[contains(@aria-label,'Filter field: "+field_name+",')]/ancestor::div[@class='columnHeader-popup sysPopup']/ancestor::body/child::div[@class='sysPopup flyoutButton-flyOut layout-root-scope']//button//span[text()='"+operator+"']"
     input_field = "//input[contains(@aria-label,'Filter field: "+field_name+",')]"
     apply_button = "//input[contains(@aria-label,'Filter field: "+field_name+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button"
     dropDown_button = "//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: "+field_name+"')]]"
     Interactions.wait_and_click(driver, By.XPATH, dropDown_button)
     Interactions.wait_and_click(driver, By.XPATH, drop_down_item)
     if(Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@class,'popupShadow popupView preview')]")):
         actions = ActionChains(driver)
         other_element = driver.find_element(By.XPATH, "//div[text()='" + field_name + "']")
         actions.move_to_element(other_element).perform()
     if operator == 'is one of' or operator == 'matches':
         new_val = Interactions.extract_multiple_values(new_val)
         for new_val_value in new_val:
             Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val_value)
             Interactions.wait_and_click(driver, By.XPATH, apply_button)
     elif operator == 'between':
         new_val = Interactions.extract_dates(new_val)
         from_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[1]"
         to_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[2]"
         Interactions.wait_and_send_keys(driver, By.XPATH, from_date_locator, new_val[0])
         Interactions.wait_and_send_keys(driver, By.XPATH, to_date_locator, new_val[1])
     else:
         Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val)
     Interactions.wait_and_click(driver, By.XPATH, apply_button)
#    "Skipping grid since it is deafault behavior of d365"
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Clicking (default) on: PurchOrder
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='PurchOrder']")
     Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'HeaderView')]")
     user_input = input('Enter the value for the hyperlink: ')
     if Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Purchase order']"):
          Interactions.wait_and_click(driver, By.XPATH,  "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Purchase order']")
          Interactions.press_enter(driver, By.XPATH, "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Purchase order']")
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Purchase order']"):
          Interactions.wait_and_click(driver, By.XPATH,  "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Purchase order']")
          Interactions.press_enter(driver, By.XPATH, "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Purchase order']")
     Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'HeaderView')]")
# going to edit view mode
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")
     time.sleep(1)
# Inputting into: PurchTable_OrderAccount
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]") ):
          #clicking inside grid: PurchTable_OrderAccount
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_OrderAccount')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]", "US-104")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Vendor account')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]", "US-104")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "US-104")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "US-104")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
# Inputting into: PurchTable_InvoiceAccount
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_InvoiceAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Invoice account')]") ):
          #clicking inside grid: PurchTable_InvoiceAccount
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InvoiceAccount')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_InvoiceAccount')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InvoiceAccount')])[1]", "US-104")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Invoice account')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Invoice account')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Invoice account')])[1]", "US-104")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_InvoiceAccount')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_InvoiceAccount')]", "US-104")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Invoice account')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Invoice account')]", "US-104")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
# Inputting into: Inventory_InventSiteId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Inventory_InventSiteId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
          #clicking inside grid: Inventory_InventSiteId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Inventory_InventSiteId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Inventory_InventSiteId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Inventory_InventSiteId')])[1]", "3")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Site')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "3")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Inventory_InventSiteId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Inventory_InventSiteId')]", "3")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "3")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
# Inputting into: Inventory_InventLocationId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Inventory_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
          #clicking inside grid: Inventory_InventLocationId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Inventory_InventLocationId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Inventory_InventLocationId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Inventory_InventLocationId')])[1]", "31")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Warehouse')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]", "31")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Inventory_InventLocationId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Inventory_InventLocationId')]", "31")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "31")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
# Inputting into: Currency_CurrencyCode
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Currency_CurrencyCode')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Currency')]") ):
          #clicking inside grid: Currency_CurrencyCode
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Currency_CurrencyCode')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Currency_CurrencyCode')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Currency_CurrencyCode')])[1]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Currency')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Currency')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Currency')])[1]", "")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Currency_CurrencyCode')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Currency_CurrencyCode')]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Currency')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Currency')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: Currency_CurrencyCode
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Currency_CurrencyCode')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Currency')]") ):
          #clicking inside grid: Currency_CurrencyCode
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Currency_CurrencyCode')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Currency_CurrencyCode')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Currency_CurrencyCode')])[1]", "USD")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Currency')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Currency')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Currency')])[1]", "USD")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Currency_CurrencyCode')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Currency_CurrencyCode')]", "USD")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Currency')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Currency')]", "USD")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
# Inputting into: Payment_Payment
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Payment_Payment')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Terms of payment')]") ):
          #clicking inside grid: Payment_Payment
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Payment_Payment')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Payment_Payment')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Payment_Payment')])[1]", "Net15")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Terms of payment')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Terms of payment')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Terms of payment')])[1]", "Net15")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Payment_Payment')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Payment_Payment')]", "Net15")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Terms of payment')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Terms of payment')]", "Net15")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
# Inputting into: Payment_PaymMode
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Payment_PaymMode')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Method of payment')]") ):
          #clicking inside grid: Payment_PaymMode
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Payment_PaymMode')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Payment_PaymMode')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Payment_PaymMode')])[1]", "CHECK")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Method of payment')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Method of payment')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Method of payment')])[1]", "CHECK")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Payment_PaymMode')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Payment_PaymMode')]", "CHECK")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Method of payment')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Method of payment')]", "CHECK")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
# Inputting into: HeaderDeliveryAddress_DeliveryName
     if(Interactions.check_element_exist(driver, By.XPATH, "//textarea[@name='HeaderDeliveryAddress_DeliveryName']")):
          Interactions.wait_and_send_keys(driver, By.XPATH, "//textarea[@name='HeaderDeliveryAddress_DeliveryName']", "Site 3")
# clicking dropdown for Tree
     Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@name,'PurchTable_DeliveryPostalAddress')]/parent::div/parent::div/following-sibling::div/div")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
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