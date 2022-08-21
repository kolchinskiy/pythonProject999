from model.contact import Contact


def test_edit_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov",
                                           mobile="88001234568", email="kolchinskiy.a@gmail.com"))
