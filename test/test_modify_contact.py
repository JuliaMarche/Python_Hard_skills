from model.contact import Contact
import random

def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="Proverka")
    random_contact = random.choice(old_contacts)
    contact.id = random_contact.id
    app.contact.modify_form_by_id(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    app.contact.old_contact_list(old_contacts, contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max())



# def test_modify_contact_homephone(app):
#     old_contacts = app.contact.get_contact_list()
#     if app.contact.count() == 0:
#         app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test"))
#     app.contact.modify_form(Contact(home="89215676577"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)

