# -*- coding: utf-8 -*-
from model.contact import Contact
import time
import random


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
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
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(2)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact.remove(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)