class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def fill_form(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.init_group_creation()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group_creation()
        self.return_to_groups_page()

    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_id("container").click()
        wd.find_element_by_link_text("groups").click()
