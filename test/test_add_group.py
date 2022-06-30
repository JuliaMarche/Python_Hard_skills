from model.group import Group
import time

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_form(Group(name="test", header="test", footer="testtest"))
    app.session.logout()
    time.sleep(0.1)
