# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.group.edit_first_group(Group(name="New_Group"))


def test_edit_header(app):
    app.group.edit_first_group(Group(header="new_header"))


def test_edit_footer(app):
    app.group.edit_first_group(Group(footer="new_footer"))