from model.group import Group


def test_edit_group(app):
    app.group.edit_first_group(Group(name="group new39", header="123456", footer="321000"))
