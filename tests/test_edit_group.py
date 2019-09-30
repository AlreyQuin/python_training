# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New_Group"))
    app.session.logout()


def test_edit_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="new_header"))
    app.session.logout()


def test_edit_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="new_footer"))
    app.session.logout()