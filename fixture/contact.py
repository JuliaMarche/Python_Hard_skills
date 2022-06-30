from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_form(self, contact):
        wd = self.app.wd
        self.init_contact_creation()
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
        self.submit_contact_creation()
        time.sleep(1)
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_to_home_page()
        wd.find_element_by_name("selected[]").click()
        time.sleep(3)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

