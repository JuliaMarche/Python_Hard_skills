from model.contact import Contact
from random import randrange

def test_delete_first_group(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
