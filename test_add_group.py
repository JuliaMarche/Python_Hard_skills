# -*- coding: utf-8 -*-
import pytest
from group import Group
from application_group import Application_group

@pytest.fixture
def app_group(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app_group):
    app_group.login(username="admin", password="secret")
    app_group.fill_group_form(Group(name="test", header="test", footer="testtest"))
    app_group.logout()
