from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, group):
        self.open_groups_page()
        self.init_group_creation()
        self.fill_group_form(group)
        self.submit_group_creation()
        self.return_to_groups_page()

    def modify_form(self, new_group_data):
        self.open_groups_page()
        self.select_first_group()
        self.edit_group()
        self.fill_group_form(new_group_data)
        self.update_group_info()
        self.return_to_groups_page()

    def delete_first_group(self):
        self.open_groups_page()
        self.select_first_group()
        self.delete_group()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_group(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def update_group_info(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def delete_group(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups