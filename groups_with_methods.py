import pytest
from group import Group
from application_groups import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="group 39", header="123", footer="321"))
    app.logout()


def test_new_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()
