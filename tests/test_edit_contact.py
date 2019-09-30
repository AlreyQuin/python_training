# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New First name",
                                    middlename="New Middle name",
                                    lastname="New Last name"))
    app.session.logout()


def test_edit_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(address="New Company Address", address2="New Address"))
    app.session.logout()


def test_edit_bdate(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(bday="22",
                                    bmonth="July",
                                    byear="2000"))
    app.session.logout()