from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from fixture.session import SessionHelper
from fixture.contact import ContactHelper

options = Options()
options.binary_location = r"C:\Users\marchenko.js\AppData\Local\Mozilla Firefox\firefox.exe"

class ApplicationContact:

    def __init__(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe', options=options)
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()