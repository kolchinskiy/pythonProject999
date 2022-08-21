from model.group import Group


def test_new_group(app):
    app.group.create(Group(name="group 39", header="123", footer="321"))


def test_new_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
