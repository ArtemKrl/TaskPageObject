from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ImagesPage(BasePage):

    ALL_SERVICES = (By.CSS_SELECTOR, 'div.services-suggest__icons-more')
    FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item:nth-child(1) > a > div:nth-child(3)")
    VALUE_SEARCH_FORM = (By.CSS_SELECTOR, ".input__control.mini-suggest__input[name='text']")
    FIRST_PICTURE = (By.CSS_SELECTOR, "div.serp-item:nth-child(1) img.serp-item__thumb")
    PICTURE_IS_OPEN = (By.CSS_SELECTOR, ".MMOrganicSnippet-TitleWrap > a")
    POPUP_WINDOW = (By.XPATH, "/html/body/div[5]/div/div/div[3]/div[3]/a[1]")
    ARROW_RIGHT = (By.CSS_SELECTOR, "div.CircleButton:nth-child(4) > i")
    ARROW_LEFT = (By.CSS_SELECTOR, ".CircleButton_type_prev")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.maximize_window()

    def name_first_category(self):
        return self.get_element_text(self.FIRST_CATEGORY)

    def open_first_category(self):
        if self.is_visible(self.POPUP_WINDOW):
            self.do_click(self.POPUP_WINDOW)
            self.do_click(self.FIRST_CATEGORY)

        else:
            self.do_click(self.FIRST_CATEGORY)

    def execute_request_value(self):
        return self.execute_value(self.VALUE_SEARCH_FORM)

    def open_first_picture(self):
        self.do_click(self.FIRST_PICTURE)
        return self.is_visible(self.PICTURE_IS_OPEN)

    def link_first_picture(self):
        return self.get_element_text(self.PICTURE_IS_OPEN)

    def link_second_picture(self):
        self.do_click(self.ARROW_RIGHT)
        return self.get_element_text(self.PICTURE_IS_OPEN)

    def back_to_first_picture(self):
        self.do_click(self.ARROW_LEFT)












