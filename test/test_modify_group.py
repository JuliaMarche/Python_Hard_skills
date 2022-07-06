from model.group import Group

def test_modify_group_name(app):
    app.group.modify_form(Group(name="New group"))

def test_modify_group_header(app):
    app.group.modify_form(Group(header="New header"))
