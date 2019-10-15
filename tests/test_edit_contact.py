# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contact = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="New First name", middlename="New Middle name", lastname="New Last name"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)


def test_edit_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contact = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(address="New Company Address", address2="New Address"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)


def test_edit_bdate(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contact = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(bday="22", bmonth="July", byear="2000"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)