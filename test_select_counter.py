from tests import login_module
import time
from selenium import webdriver


class TestSelectCounter:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login_module.login_inspector(driver)

    def teardown(self):
        self.driver.quit()

    def test_select_counter(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[2]/a').click()
        driver.find_element_by_class_name('input-group-addon').click()
        counter = driver.find_element_by_xpath('//li[@data-value="вулиця Ковельська 1, Чернівці, Чернівецька область"]')
        counter.click()
        time.sleep(1)
        assert driver.find_element_by_xpath\
            ('//*[@id="countersTable"]//td[contains(text(),"ДнепрОблЭнерго")]') \
            .is_displayed()
        assert driver.find_element_by_class_name("change-value").is_displayed()
        assert driver.find_element_by_class_name("change-value").is_enabled()
        assert driver.find_element_by_class_name("change-status").is_displayed()
        assert driver.find_element_by_class_name("change-status").is_enabled()

