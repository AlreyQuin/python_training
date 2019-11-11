# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_name(app, db, json_contacts, check_ui):
    contact = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contact = db.get_contact_list()
    c = random.choice(old_contact)
    app.contact.edit_contact_by_id(contact, c.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    contact.id = c.id
    old_contact.remove(c)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)
