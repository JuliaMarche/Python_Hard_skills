def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test", title="Test", company="Test", address="Test", home="Test", work="Test", email="Test", bday="19", bmonth="June", byear="1994", address2="Test", notes="Test"))
    app.session.logout()