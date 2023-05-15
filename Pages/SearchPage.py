from selenium.webdriver.common.by import By
from Pages.ImagesPage import ImagesPage
from config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys



class SearchPage(BasePage):

    SEARCH_FORM = (By.CSS_SELECTOR, "#text")
    PROMPT_MENU = (By.CSS_SELECTOR, "ul.mini-suggest__popup-content")
    SEARCH_RESULT_PAGE = (By.CSS_SELECTOR, "[aria-label='Результаты поиска']")
    LINK_IN_SEARCH = (By.CSS_SELECTOR, ".Organic-Path_verified > a:nth-child(1) > b:nth-child(1)")
    ALL_SERVICES = (By.CSS_SELECTOR, 'div.services-suggest__icons-more')
    PICTURES_SERVICE = (By.XPATH, "//div[@aria-hidden='true' and text()='Картинки']")
    FIRST_CATEGORY = (By.CSS_SELECTOR, "div.search2__input")



    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()


    def open_first_category(self):
        self.do_click(self.FIRST_CATEGORY)
    def is_search_form_visible(self):
        return self.is_visible(self.SEARCH_FORM)

    def open_search_form(self):
        self.do_click(self.SEARCH_FORM)

    def enter_text_request(self, text_request):
        self.do_send_keys(self.SEARCH_FORM, text_request)

    def is_prompt_visible(self):
        return self.is_visible(self.PROMPT_MENU)

    def push_enter_button(self):
        self.do_push_buttons(self.SEARCH_FORM, Keys.ENTER)

    def search_result_visible(self):
       return self.is_visible(self.SEARCH_RESULT_PAGE)

    def link_execute(self):
        return self.get_element_text(self.LINK_IN_SEARCH)

    def is_all_services_visible(self):
        return self.is_visible(self.ALL_SERVICES)

    def open_all_services(self):
        self.do_click(self.ALL_SERVICES)

    def pictures_open(self):
        self.do_click(self.PICTURES_SERVICE)
        # images_window_handle = self.driver.window_handles[1]
        imagesPage = ImagesPage(self.driver)
        # imagesPage.switch_to_window(images_window_handle)
        return imagesPage

    def clicable_elem(self):
        return self.is_clickable(self.FIRST_CATEGORY)
