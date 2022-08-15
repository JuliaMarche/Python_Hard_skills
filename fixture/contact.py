import re

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
        self.edit_contact_index(index)
        self.info_from_form(new_contact_data)
        self.update_contact_info()
        self.return_after_modify()
        self.contact_cache = None

    def modify_form_by_id(self, new_contact_data):
        self.open_to_home_page()
        self.edit_contact_id(new_contact_data.id)
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_to_home_page()
        self.select_contact_by_id(id)
        self.delete_contact()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def open_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath('//*[@title="Details"]')) > 0):
            wd.find_element_by_link_text("home").click()

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_contact_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath('//*[@title="Edit"]')[index].click()

    def edit_contact_id(self, id):
        wd = self.app.wd
        for row in wd.find_elements_by_name("entry"):
            cell = row.find_elements_by_tag_name("td")[7]
            cells = cell.find_element_by_xpath("./a[@href]").get_attribute("href")
            id_number = cells.split("id=")[1]
            if id_number == str(id):
                cell.find_element_by_tag_name("a").click()
                break

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        for row in wd.find_elements_by_name("entry"):
            cell = row.find_elements_by_tag_name("td")[7]
            cells = cell.find_element_by_xpath("./a[@href]").get_attribute("href")
            id_number = (cells.split("id=")[1])
            if id_number == str(id):
                break

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
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.second_email)
        self.change_field_value("email3", contact.third_email)
        self.change_field_value("address2", contact.second_address)
        self.change_field_value("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.open_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  address=address, all_phones_from_home_page=all_phones,
                                                  all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd. find_element_by_name("email").get_attribute("value")
        second_email = wd. find_element_by_name("email2").get_attribute("value")
        third_email = wd. find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, homephone=homephone,
                       workphone=workphone, mobile=mobile, secondphone=secondphone, email=email,
                       second_email=second_email, third_email=third_email)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        secondphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobile=mobile, secondphone=secondphone)

    def old_contact_list(self, contacts, contact):
        n = -1
        for i in range(len(contacts)):
            c = contacts[i]
            if c.id == contact.id:
                n = i
                break
        contacts[n] = contact