# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

options = Options()
options.binary_location = r'C:\Users\marchenko.js\AppData\Local\Mozilla Firefox\firefox.exe'

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe', options=options)
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, name="test", header="test", footer="testtest")
        self.submit_group_creation(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()
        time.sleep(1)

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()
        time.sleep(1)

    def fill_group_form(self, wd, name, header, footer):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        time.sleep(1)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        time.sleep(1)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        time.sleep(1)

    def init_group_creation(self, wd):
        wd.find_element_by_name("new").click()

    def open_groups_page(self, wd):
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        time.sleep(1)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        time.sleep(2)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
