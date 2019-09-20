# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New_Group", header="new_header", footer="new_footer"))
    app.session.logout()