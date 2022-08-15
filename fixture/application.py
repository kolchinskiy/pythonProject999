from selenium import webdriver
from fixture.session_helper import SessionHelper
from fixture.group_contact_helper import GroupContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupContactHelper(self)
        self.contact = GroupContactHelper(self)

    def open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
