from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test", title="Test",
                      company="Test", address="Test", homephone="88888888", workphone="888888888",
                      mobile="88888888888", email="Test", second_email="Test@test.ru", bday="19", bmonth="June",
                      byear="1994", second_address="Test", notes="Test")
    app.contact.fill_form(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
