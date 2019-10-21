# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    days = []
    for i in range(1, 32):
        days.append(i)
    return str(random.choice(days))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return random.choice(months)


def random_email(maxlen):
    e = string.ascii_letters + string.digits
    mail = string.ascii_letters + string.digits + "."
    return "".join([random.choice(e) for i in range(random.randrange(maxlen))]) + "@".join([random.choice(mail) for i in range(random.randrange(maxlen))])


def random_site(maxlen):
    site = string.ascii_letters + string.digits
    return "www" + "".join([random.choice(site) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string(6),
                    middlename=random_string(4),
                    lastname=random_string(9),
                    nickname=random_string(8),
                    title=random_string(20),
                    company=random_string(8),
                    address=random_string(30),
                    home=random_number(9),
                    mobile=random_number(9),
                    work=random_number(9),
                    fax=random_number(9),
                    email=random_email(6),
                    email2=random_email(5),
                    email3=random_email(4),
                    homepage=random_site(10),
                    bday=random_day(),
                    bmonth=random_month(),
                    byear=random_number(4),
                    address2=random_string(35),
                    phone2=random_number(10),
                    notes=random_string(15))]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

