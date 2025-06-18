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
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
# Inputting into: PurchTable_OrderAccount
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]") ):
          #clicking inside grid: PurchTable_OrderAccount
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_OrderAccount')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]", "US_TX_020")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Vendor account')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]", "US_TX_020")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "US_TX_020")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "US_TX_020")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
# Inputting into: editContactPersonName
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'editContactPersonName')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Contact')]") ):
          #clicking inside grid: editContactPersonName
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'editContactPersonName')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'editContactPersonName')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'editContactPersonName')])[1]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Contact')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Contact')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Contact')])[1]", "")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'editContactPersonName')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'editContactPersonName')]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Contact')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Contact')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: PurchTable_InventSiteId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventSiteId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
          #clicking inside grid: PurchTable_InventSiteId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventSiteId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_InventSiteId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventSiteId')])[1]", "4")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Site')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "4")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventSiteId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventSiteId')]", "4")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "4")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
# Inputting into: PurchTable_InventLocationId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
          #clicking inside grid: PurchTable_InventLocationId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventLocationId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_InventLocationId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventLocationId')])[1]", "48")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Warehouse')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]", "48")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]", "48")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "48")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
# Inputting into: PurchTable_InventLocationId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
          #clicking inside grid: PurchTable_InventLocationId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventLocationId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_InventLocationId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_InventLocationId')])[1]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Warehouse')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]", "")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_InventLocationId')]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: editPurchAgreementId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'editPurchAgreementId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]") ):
          #clicking inside grid: editPurchAgreementId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'editPurchAgreementId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'editPurchAgreementId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'editPurchAgreementId')])[1]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase agreement')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase agreement')])[1]", "")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'editPurchAgreementId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'editPurchAgreementId')]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase agreement')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: groupAdministraton_ItemBuyerGroupId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'groupAdministraton_ItemBuyerGroupId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Buyer group')]") ):
          #clicking inside grid: groupAdministraton_ItemBuyerGroupId
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'groupAdministraton_ItemBuyerGroupId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'groupAdministraton_ItemBuyerGroupId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'groupAdministraton_ItemBuyerGroupId')])[1]", "10")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Buyer group')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Buyer group')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Buyer group')])[1]", "10")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'groupAdministraton_ItemBuyerGroupId')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'groupAdministraton_ItemBuyerGroupId')]", "10")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Buyer group')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Buyer group')]", "10")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
# clicking dropdown for Tree
     Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@name,'groupAdministraton_Requester')]/parent::div/parent::div/following-sibling::div/div")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Inputting into: PurchTable_ConfirmingPO_ConfirmingPOID
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_ConfirmingPO_ConfirmingPOID')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Confirming PO')]") ):
          #clicking inside grid: PurchTable_ConfirmingPO_ConfirmingPOID
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_ConfirmingPO_ConfirmingPOID')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_ConfirmingPO_ConfirmingPOID')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_ConfirmingPO_ConfirmingPOID')])[1]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Confirming PO')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Confirming PO')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Confirming PO')])[1]", "")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_ConfirmingPO_ConfirmingPOID')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_ConfirmingPO_ConfirmingPOID')]", "")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Confirming PO')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Confirming PO')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OK']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
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
     user_input = input('Enter the value for the hyperlink: ')
     if Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Item number']"):
          Interactions.wait_and_click(driver, By.XPATH,  "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Item number']")
          Interactions.press_enter(driver, By.XPATH, "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Item number']")
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Item number']"):
          Interactions.wait_and_click(driver, By.XPATH,  "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Item number']")
          Interactions.press_enter(driver, By.XPATH, "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Item number']")
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
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OkCommandButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OkCommandButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkCommandButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkCommandButton']")
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]") ):
         #clicking inside grid: PurchLine_PurchQtyGrid
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]", "5.00")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Quantity')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])[1]", "5.00")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_PurchQtyGrid')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]", "5.00")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Quantity')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]", "5.00")
          Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]") ):
         #clicking inside grid: PurchLine_PurchReceivedNow
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchReceivedNow')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])[1]", "3.00")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Receive now')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])[1]", "3.00")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_PurchReceivedNow')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]", "3.00")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Receive now')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]", "3.00")
          Interactions.press_enter(driver, By.XPATH, "//body")
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