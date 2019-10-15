# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="First name",
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
                                    notes="Notes")
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

