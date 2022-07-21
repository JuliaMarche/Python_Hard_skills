from model.contact import Contact
from random import randrange

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Proverka")
    contact.id = old_contacts[index].id
    app.contact.modify_form_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_homephone(app):
#     old_contacts = app.contact.get_contact_list()
#     if app.contact.count() == 0:
#         app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test"))
#     app.contact.modify_form(Contact(home="89215676577"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)

