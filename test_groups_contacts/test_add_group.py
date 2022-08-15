from model.group import Group


def test_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="group 39", header="123", footer="321"))
    app.session.logout()


def test_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="", header="", footer=""))
    app.session.logout()
