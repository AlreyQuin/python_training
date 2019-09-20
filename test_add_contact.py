# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="First name",
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
    app.logout()

