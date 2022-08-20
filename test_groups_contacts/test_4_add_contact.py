from model.contact import Contact


def test_new_address(app):
    app.contact.create_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", mobile="88001234567"
                                       , email="artem94@list.ru"))
