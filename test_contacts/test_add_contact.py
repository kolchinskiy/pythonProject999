import pytest
from model_contacts.contact import Contact
from fixture_contacts.application_contacts import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_address(app):
    app.session.login()
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", mobile="88001234567",
                               email="ivanov@mail.ru"))
    app.session.logout()