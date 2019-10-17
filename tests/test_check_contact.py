import re
from random import randrange


def test_contact_on_homepade(app):
    list_contact = app.contact.get_contact_list()
    index = randrange(len(list_contact))
    if index != 0:
        contact_from_homepage = app.contact.get_contact_list()[index]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        assert contact_from_homepage.lastname == contact_from_edit_page.lastname
        assert contact_from_homepage.firstname == contact_from_edit_page.firstname
        assert contact_from_homepage.address == contact_from_edit_page.address
        assert contact_from_homepage.all_email_from_hp == merge_email_like_on_hp(contact_from_edit_page)
        assert contact_from_homepage.all_phones_from_hp == merge_phones_like_on_hp(contact_from_edit_page)


def test_contact_on_view_pade(app):
    list_contact = app.contact.get_contact_list()
    index = randrange(len(list_contact))
    if index != 0:
        contact_from_view_page = app.contact.get_contact_from_view_page(index)
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        fullnamestr = str(contact_from_view_page.fullname)
        assert fullnamestr.startswith(contact_from_edit_page.firstname)
        assert fullnamestr.endswith(contact_from_edit_page.lastname)
        assert contact_from_view_page.home == contact_from_edit_page.home
        assert contact_from_view_page.mobile == contact_from_edit_page.mobile
        assert contact_from_view_page.work == contact_from_edit_page.work
        assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[- _()]", "", s)

def merge_phones_like_on_hp(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_email_like_on_hp(contact):
    return "\n".join(filter(lambda x: x != "", (filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))

