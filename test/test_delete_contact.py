from model.contact import Contact
def test_delete_first_group(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test"))
    app.contact.delete_first_contact()
