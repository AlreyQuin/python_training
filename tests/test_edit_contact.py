# -*- coding: utf-8 -*-
from model.contact import Contact

cont = Contact(firstname="First name",
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


def test_edit_name(app):
    if app.contact.count() == 0:
        app.contact.create(cont)
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="New First name", middlename="New Middle name", lastname="New Last name")
    contact.id = old_contact[0].id
    app.contact.edit_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_edit_address(app):
#    if app.contact.count() == 0:
#        app.contact.create(cont)
#    old_contact = app.contact.get_contact_list()
#    contact = Contact(address="New Company Address", address2="New Address")
#    app.contact.edit_first_contact(contact)
#    new_contact = app.contact.get_contact_list()
#    assert len(old_contact) == len(new_contact)


#def test_edit_bdate(app):
#   if app.contact.count() == 0:
#        app.contact.create(cont)
#    old_contact = app.contact.get_contact_list()
#    contact = Contact(bday="22", bmonth="July", byear="2000")
#    app.contact.edit_first_contact(contact)
#    new_contact = app.contact.get_contact_list()
#    assert len(old_contact) == len(new_contact)