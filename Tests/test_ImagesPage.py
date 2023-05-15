import allure
from Pages.SearchPage import SearchPage
from Tests.test_base import BaseTest
from config.config import TestData


@allure.feature("Images")
class Test_Images(BaseTest):

    @allure.story("Open Yandex Images")
    def test_yandex_images(self):
        self.searchPage = SearchPage(self.driver)
        self.searchPage.open_search_form()
        # проверка, что кнопка "все сервисы" присутствует на странице
        assert self.searchPage.is_all_services_visible()
        self.searchPage.open_all_services()
        imagesPage = self.searchPage.pictures_open()
        # проверка, что перешли на url https://yandex.ru/images/
        assert imagesPage.get_current_url(TestData.EXPECTED_URL)
        name_first_category = imagesPage.name_first_category()
        imagesPage.open_first_category()
        search_request = imagesPage.execute_request_value()
        # проверка, что название категории присутствует в поле поиска
        assert name_first_category == search_request
        # проверка, что первая картинка открывается
        imagesPage.open_first_picture()
        get_first_picture = imagesPage.link_first_picture()
        get_second_picture = imagesPage.link_second_picture()
        # проверка, что открылась вторая картинка
        assert get_first_picture != get_second_picture
        imagesPage.back_to_first_picture()
        back_to_first_picture = imagesPage.link_first_picture()
        # проверка, что после возврата снова открылась первая картинка
        assert get_first_picture == back_to_first_picture
