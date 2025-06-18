# base.py
from selenium import webdriver
import time
import login
from selenium.webdriver.common.action_chains import ActionChains

class BaseTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(3)
        login.login(self.driver)
        self.ActionChains = ActionChains(self.driver)
        # Shared attributes
        # self.locator = ""
        self.filter_manager_column_last_opened = ""
        self.filter_manager_dropdown_item_index = 1
        self.column_to_open = ""
        self.user_input = None
        # self.save_line_items_without_errors = False
        self.test_passed = True
