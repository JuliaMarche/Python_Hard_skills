from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test"))
    app.contact.modify_form(Contact(firstname="Proverka"))

def test_modify_contact_homephone(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test"))
    app.contact.modify_form(Contact(home="89215676577"))

