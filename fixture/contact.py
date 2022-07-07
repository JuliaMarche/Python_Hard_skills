from selenium.webdriver.support.select import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, contact):
        self.open_to_home_page()
        self.init_contact_creation()
        self.info_from_form(contact)
        self.submit_contact_creation()
        self.return_to_home_page()

    def modify_form(self, new_contact_data):
        self.open_to_home_page()
        self.edit_contact()
        self.info_from_form(new_contact_data)
        self.update_contact_info()
        self.return_after_modify()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_to_home_page()
        self.select_first_contact()
        self.delete_contact()
        wd.switch_to.alert.accept()

    def open_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@title="Edit"]').click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def update_contact_info(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def return_after_modify(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def info_from_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.company_address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("bday", contact.bday)
        self.change_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("notes", contact.notes)

        # wd.find_element_by_name("middlename").click()
        # wd.find_element_by_name("middlename").clear()
        # wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # wd.find_element_by_name("lastname").click()
        # wd.find_element_by_name("lastname").clear()
        # wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # wd.find_element_by_name("nickname").click()
        # wd.find_element_by_name("nickname").clear()
        # wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # wd.find_element_by_name("title").click()
        # wd.find_element_by_name("title").clear()
        # wd.find_element_by_name("title").send_keys(contact.title)
        # wd.find_element_by_name("company").click()
        # wd.find_element_by_name("company").clear()
        # wd.find_element_by_name("company").send_keys(contact.company)
        # wd.find_element_by_name("address").click()
        # wd.find_element_by_name("address").clear()
        # wd.find_element_by_name("address").send_keys(contact.company_address)
        # wd.find_element_by_name("home").click()
        # wd.find_element_by_name("home").clear()
        # wd.find_element_by_name("home").send_keys(contact.home_phone)
        # wd.find_element_by_name("work").click()
        # wd.find_element_by_name("work").clear()
        # wd.find_element_by_name("work").send_keys(contact.work_phone)
        # wd.find_element_by_name("email").click()
        # wd.find_element_by_name("email").clear()
        # wd.find_element_by_name("email").send_keys(contact.email)
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys(contact.byear)
        # wd.find_element_by_name("address2").click()
        # wd.find_element_by_name("address2").clear()
        # wd.find_element_by_name("address2").send_keys(contact.address2)
        # wd.find_element_by_name("notes").click()
        # wd.find_element_by_name("notes").clear()
        # wd.find_element_by_name("notes").send_keys(contact.notes)