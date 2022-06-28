# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application_group import ApplicationGroup

@pytest.fixture
def app_group(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app_group):
    app_group.session.login(username="admin", password="secret")
    app_group.group.fill_form(Group(name="test", header="test", footer="testtest"))
    app_group.session.logout()
