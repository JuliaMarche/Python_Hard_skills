from model.contact import Contact


def test_edit_contact(app):
    print(app)
    app.session.login(username="admin", password="secret")
    app.contact.modify_form(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test", title="Test",
                                    company="Test", address="Test", home="Test", work="Test", email="Test", bday="19",
                                    bmonth="June", byear="1994", address2="Test", notes="Test"))
    app.session.logout()
