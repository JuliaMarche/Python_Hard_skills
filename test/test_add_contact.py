from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone():
    phone = "8" + "".join(random.choice(string.digits) for i in range(10))
    return phone

def random_email():
    email = string.ascii_letters + string.digits
    return "".join(random.choice(email) for i in range(7)) + "@mail.test"

testdata = [Contact(firstname="", lastname="", mobile="", email="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), title=random_string("title", 10),
            company=random_string("company", 10), address=random_string("address", 10), homephone=random_phone(),
            workphone=random_phone(), mobile=random_phone(), secondphone=random_phone(),
            email=random_email(), second_email=random_email(), bday="19", bmonth="June",
            byear="1994", second_address=random_string("second_address", 10), notes=random_string("notes", 10))
for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_form(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
