import re
from model.contact import Contact

def test_contact_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test", homephone="888888345888", workphone="888845368888",
                                      mobile="888884536888", secondphone="888854638888", email="Test",
                                      second_email="Test1", address="Test", third_email="Test2"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == marge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_contact_page_and_db(app, db):
    if app.contact.count() == 0:
        app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test", homephone="888888345888", workphone="888845368888",
                                      mobile="888884536888", secondphone="888854638888", email="Test",
                                      second_email="Test1", address="Test", third_email="Test2"))
    contacts_homepage = app.contact.get_contact_list()
    contacts_db = db.get_contact_list()
    contacts_homepage = sorted(contacts_homepage, key=Contact.id_or_max)
    contacts_db = sorted(contacts_db, key = Contact.id_or_max)
    assert len(contacts_homepage) == len (contacts_db)
    for i in range(len(contacts_homepage)):
        c_hp = contacts_homepage[i]
        c_db = contacts_db[i]
        assert clear_spaces(c_hp.firstname) == clear_spaces(c_db.firstname)
        assert clear_spaces(c_hp.lastname) == clear_spaces(c_db.lastname)
        assert clear_spaces(c_hp.address) == clear_spaces(c_db.address)
        assert c_hp.all_phones_from_home_page == marge_phones_like_on_home_page(c_db)
        assert c_hp.all_email_from_home_page == merge_emails_like_on_home_page(c_db)


def test_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.secondphone == contact_from_edit_page.secondphone


def clear(s):
    return re.sub("[() -]", "", s)

def clear_spaces(s):
    while s.find('  ') != -1:
        s = s.replace('  ', ' ')

def marge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.secondphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (filter(lambda x: x is not None,
                                    [contact.email, contact.second_email, contact.third_email]))))
