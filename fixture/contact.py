from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, contact):
        self.open_to_home_page()
        self.init_contact_creation()
        self.info_from_form(contact)
        self.submit_contact_creation()
        self.open_to_home_page()
        self.contact_cache = None

    def modify_form(self):
        self.modify_form_by_index(0)

    def modify_form_by_index(self, new_contact_data, index):
        self.open_to_home_page()
        self.edit_contact(index)
        self.info_from_form(new_contact_data)
        self.update_contact_info()
        self.return_after_modify()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_to_home_page()
        self.select_contact_by_index(index)
        self.delete_contact()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.

    def open_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath('//*[@title="Details"]')) > 0):
            wd.find_element_by_link_text("home").click()

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath('//*[@title="Edit"]')[index].click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def update_contact_info(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def return_after_modify(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath('//*[@title="Details"]')) > 0):
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
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("phone2", contact.second_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.open_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                cells_firstname = cells[2]
                cells_lastname = cells[1]
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=cells_firstname.text, lastname=cells_lastname.text, id=id))
        return list(self.contact_cache)

