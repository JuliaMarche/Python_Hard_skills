from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
import unittest, time
from contact import Contact

options = Options()
options.binary_location = r"C:\Users\marchenko.js\AppData\Local\Mozilla Firefox\firefox.exe"

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe', options=options)
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_contact_creation(wd)
        self.fill_contact_form(wd, Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test", title="Test", company="Test", address="Test", home="Test", work="Test", email="Test", bday="19", bmonth="June", byear="1994", address2="Test", notes="Test"))
        self.submit_contact_creation(wd)
        time.sleep(1)
        self.return_to_home_page(wd)
        time.sleep(2)
        self.logout(wd)


    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def submit_contact_creation(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, wd, contact):
        # Add firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # Add middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # Add lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # Add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(contact.title)
        # Add company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys(contact.company)
        # Add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(contact.company_address)
        # Add home_phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        # Add work_phone
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        # Add email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(contact.email)
        # Choose birthday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # Add address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        # Add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def init_contact_creation(self, wd):
        wd.find_element_by_link_text("add new").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

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
