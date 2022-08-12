from model.group import Group
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.fill_form(Group(name="Test"))
    old_groups = db.get_group_list()
    group = Group(name="New group")
    random_group = random.choice(old_groups)
    group.id = random_group.id
    app.group.modify_form_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    app.group.old_groups_list(old_groups, group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.fill_form(Group(name="Test"))
#     app.group.modify_form(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
