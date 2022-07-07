from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.fill_form(Group(name="Test"))
    app.group.modify_form(Group(name="New group"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.fill_form(Group(name="Test"))
    app.group.modify_form(Group(header="New header"))
