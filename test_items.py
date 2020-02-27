import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_exist(browser):
    browser.get(link)
    time.sleep(30)
    button1=browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert len(button1.text) >0, "Button 'Add to busket' not exist"