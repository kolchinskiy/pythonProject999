import pytest
from contact import Contact
from application_contacts import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_address(app):
    app.login()
    app.create_address(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", mobile="88001234567",
                        email="ivanov@mail.ru"))
    app.logout()