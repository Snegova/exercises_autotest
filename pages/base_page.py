# сделаем базовую страницу, от которой будут унаследованы все остальные классы
# В ней мы опишем вспомогательные методы для работы с драйвером.
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):       # так объявляется конструктор-метод, который вызывают при создании объекта
        self.browser = browser              # в качестве параметров мы передаем экземпляр драйвера и url адрес.
        self.url = url                      # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
        self.browser.implicitly_wait(timeout)
    def open(self):                         #метод open открывает нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)

    def is_element_present(self, how, what): # метод для перехватывания исключений
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True