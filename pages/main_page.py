from .base_page import BasePage    # делаем импорт базового класса BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):          # создаем класс MainPage. Делаем его наследником класса BasePage, чтобы он имел доступ к методам и атрибутам предка
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"