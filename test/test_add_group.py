from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test", header="test", footer="testtest")
    app.group.fill_form(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert old_groups == new_groups
