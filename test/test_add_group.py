from model.group import Group

def test_add_group(app):
    app.group.fill_form(Group(name="test", header="test", footer="testtest"))
