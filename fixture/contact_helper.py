class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_link_text("add new").click()
        self.complete_form(contact)
        wd.find_element_by_name("submit").click()
        self.app.open_main_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_main_page()
        # push_the_button_Edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.complete_form(contact)
        # saving_new_form
        wd.find_element_by_name("update").click()
        self.app.open_main_page()

    def complete_form(self, contact):
        self.change_fiend_value("firstname", contact.firstname)
        self.change_fiend_value("middlename", contact.middlename)
        self.change_fiend_value("lastname", contact.lastname)
        self.change_fiend_value("mobile", contact.mobile)
        self.change_fiend_value("email", contact.email)

    def change_fiend_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_main_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete selected contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # approve deletion
        wd.switch_to.alert.accept()

    def count(self):
        wd = self.app.wd
        self.app.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))
