from model.contact import Contact


def test_new_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.delete_first_contact()
