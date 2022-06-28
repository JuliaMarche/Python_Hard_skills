import pytest
from model.contact import Contact
from fixture.application_contact import Application_contact

@pytest.fixture
def app_contact(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app_contact):
    app_contact.login(username="admin", password="secret")
    app_contact.fill_contact_form(Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test", title="Test", company="Test", address="Test", home="Test", work="Test", email="Test", bday="19", bmonth="June", byear="1994", address2="Test", notes="Test"))
    app_contact.logout()
