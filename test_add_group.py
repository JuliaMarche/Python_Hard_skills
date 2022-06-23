# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.select import Select
import unittest, time
from group import Group

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

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
        self.fill_group_form(wd, Group(name="test", header="test", footer="testtest"))
        self.submit_group_creation(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_contact_creation(wd)
        self.fill_contact_form(wd)
        self.submit_contact_creation(wd)
        time.sleep(1)
        self.return_to_home_page(wd)
        time.sleep(1)
        self.logout(wd)


    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def submit_contact_creation(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, wd):
        # Add firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("Test")
        # Add middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys("Test")
        # Add lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys("Test")
        # Add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys("Test")
        # Add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys("Test test")
        # Add company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys("Test")
        # Add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys("Test test test")
        # Add home
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys("Test")
        # Add work
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys("Test")
        # Add email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys("test@test.test")
        # Choose birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("//option[@value='19']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("//option[@value='June']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys("1994")
        # Add address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys("test")
        # Add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys("comment")

    def init_contact_creation(self, wd):
        wd.find_element_by_link_text("add new").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()
        time.sleep(1)

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()
        time.sleep(1)

    def fill_group_form(self, wd, group):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        time.sleep(1)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").send_keys(group.header)
        time.sleep(1)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
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
