from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="group new39", header="123456", footer="321000"))
    app.session.logout()
