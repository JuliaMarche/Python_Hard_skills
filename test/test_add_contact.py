from model.contact import Contact

def test_add_contact(app):
    app.contact.fill_form(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test", title="Test", company="Test", address="Test", home="Test", work="Test", email="Test", bday="19", bmonth="June", byear="1994", address2="Test", notes="Test"))
