from tests import login_module
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class TestChangeUserRole:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login_module.login_admin(driver)

    def teardown(self):
        self.driver.quit()

    def test_change_role(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[2]/a').click()
        time.sleep(1)
        assert driver.find_element_by_xpath\
            ('//*[@id="users-table"]//td[contains(text(),"Chuikina")]//..//td[contains(text(),"Mariya")]')\
            .is_displayed()

        users_table = driver.find_element_by_id("users-table")
        users = users_table.find_elements_by_tag_name("tr")
        found_user = False
        for user in users:
            cols = user.find_elements_by_tag_name("td")
            for col in cols:
                if col.text == "Chuikina":
                    user.find_element_by_class_name("btn-success").click()
                    time.sleep(1)
                    select = Select(driver.find_element_by_id("role"))
                    select.select_by_visible_text("ADMIN")
                    driver.find_element_by_id("updateRole").click()
                    time.sleep(1)
                    found_user = True
                    break
            if found_user:
                break
        assert driver.find_element_by_xpath('//*[@id="users-table"]//td[contains(text(),"Chuikina")]//..//td[contains(text(),"ADMIN")]').is_displayed()

