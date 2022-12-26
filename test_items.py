import unittest
import pytest
from selenium.webdriver.common.by import By
import time

def test_guest_should_see_add_to_basket_button(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5) # это вроде было опционально, но я решила облегчить тебе проверку :)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket"), "Oh no!!! I can't found this button!!!"

if __name__ == "__main__":
    unittest.main()

