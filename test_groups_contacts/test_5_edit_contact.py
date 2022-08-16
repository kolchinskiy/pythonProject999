from model.contact import Contact


def test_edit_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov",
                                           mobile="88001234568", email="kolchinskiy.a@gmail.com"))
    app.session.logout()
