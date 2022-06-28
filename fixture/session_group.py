
class SessionHelper_group:

    def __init__(self, app_group):
        self.app_group = app_group


    def login(self, username, password):
        wd = self.app_group.wd
        self.app_group.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app_group.wd
        wd.find_element_by_link_text("Logout").click()