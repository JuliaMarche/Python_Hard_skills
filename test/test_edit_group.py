from model.group import Group
import time

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_form(Group(name="Test", header="Edit", footer="Edit"))
    app.session.logout()
    time.sleep(0.1)