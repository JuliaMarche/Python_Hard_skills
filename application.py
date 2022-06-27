from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest, time

options = Options()
options.binary_location = r"C:\Users\marchenko.js\AppData\Local\Mozilla Firefox\firefox.exe"

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe', options=options)
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()
        time.sleep(1)

    def submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()
        time.sleep(1)

    def fill_group_form(self, group):
        wd = self.wd
        self.open_groups_page()
        self.init_group_creation()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        time.sleep(1)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").send_keys(group.header)
        time.sleep(1)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        time.sleep(1)
        self.submit_group_creation()
        self.return_to_groups_page()

    def init_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        time.sleep(1)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        time.sleep(2)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy (self):
        self.wd.quit()