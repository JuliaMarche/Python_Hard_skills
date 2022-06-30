from model.contact import Contact
import time

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_form(Contact(firstname="Julia", middlename="Test", lastname="Edit", nickname="Test", title="Proverka", company="Test", address="Test", home="956543645", work="898457735", email="Test", bday="19", bmonth="June", byear="1994", address2="Test", notes="Test"))
    app.session.logout()
    time.sleep(0.1)
