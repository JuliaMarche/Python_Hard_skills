from model.group import Group

def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.fill_form(Group(name="Test"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[0:1] = []
    assert old_groups == new_groups
