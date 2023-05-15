
import allure
from config.config import TestData
from Pages.SearchPage import SearchPage
from Tests.test_base import BaseTest

@allure.feature("Search")
class Test_Search(BaseTest):

    @allure.story("Using Yandex Search")
    def test_search_in_yandex(self):
        self.searchPage = SearchPage(self.driver)
        # проверка наличия поля поиска
        assert self.searchPage.is_search_form_visible()
        self.searchPage.open_search_form()
        self.searchPage.enter_text_request(TestData.TEXT_REQUEST)
        # проверка наличия меню подсказок
        assert self.searchPage.is_prompt_visible()
        self.searchPage.push_enter_button()
        # Проверка открытия страницы с результатами поиска
        assert self.searchPage.search_result_visible()
        # Проверка, что первая ссылка ведёт на сайт tensor.ru
        assert self.searchPage.link_execute() == TestData.LINK_TENSOR

