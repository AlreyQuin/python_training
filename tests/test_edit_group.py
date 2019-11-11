# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_group(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test_header", footer="test_footer"))
    old_groups = db.get_group_list()
    gr = random.choice(old_groups)
    app.group.edit_group_by_id(group, gr.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.id = gr.id
    old_groups.remove(gr)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



