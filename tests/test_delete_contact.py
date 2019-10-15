# -*- coding: utf-8 -*-
from model.contact import Contact
import time
from random import randrange


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First name",
                                    middlename="Middle name",
                                    lastname="Last name",
                                    nickname="Nickname",
                                    title="Title",
                                    company="Company",
                                    address="Company Address",
                                    home="Home phone",
                                    mobile="Mobile phone",
                                    work="Work phone",
                                    fax="Fax",
                                    email="E-mail",
                                    email2="E-mail-2",
                                    email3="E-mail-3",
                                    homepage="Homepage",
                                    bday="17",
                                    bmonth="September",
                                    byear="2000",
                                    address2="Address",
                                    phone2="Home",
                                    notes="Notes"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    time.sleep(2)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[0:1] = []
    assert old_contact == new_contact