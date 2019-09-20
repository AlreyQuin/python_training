# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New First name",
                                    middlename="New Middle name",
                                    lastname="New Last name",
                                    nickname="New Nickname",
                                    title="New Title",
                                    company="New Company",
                                    address="New Company Address",
                                    home="New Home phone",
                                    mobile="New Mobile phone",
                                    work="New Work phone",
                                    fax="New Fax",
                                    email="New E-mail",
                                    email2="New E-mail-2",
                                    email3="New E-mail-3",
                                    homepage="New Homepage",
                                    bday="20",
                                    bmonth="September",
                                    byear="2000",
                                    address2="New Address",
                                    phone2="New Home",
                                    notes="New Notes"))
    app.session.logout()