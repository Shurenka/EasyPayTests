from tests import login_module
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class TestSetNewCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login_module.login_inspector(driver)

    def teardown(self):
        self.driver.quit()

    def test_set_new_value(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="sidebar-menu"]/div/ul/li[2]/a').click()
        driver.find_element_by_class_name('input-group-addon').click()
        counter = driver.find_element_by_xpath('//li[@data-value="вулиця Ковельська 1, Чернівці, Чернівецька область"]')
        counter.click()
        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.ID, 'countersTable')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        prev_value = int(driver.find_element_by_class_name("oldValue").text)
        driver.find_element_by_class_name("change-value").click()
        new_value_field = driver.find_element_by_id("newCurrentValue")
        apply_button = driver.find_element_by_class_name("js-apply")
        new_value_field.send_keys("-1")
        apply_button.click()
        assert driver.find_element_by_id("wrong-value").is_displayed()
        new_value_field.clear()
        new_value_field.send_keys(prev_value-1)
        apply_button.click()
        assert driver.find_element_by_id("wrong-value").is_displayed()
        new_value_field.clear()
        new_value_field.send_keys(prev_value + 1)
        apply_button.click()
        try:
            WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.ID, 'countersTable')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        current_value = int(driver.find_element_by_class_name("counter-value").text)
        assert current_value == prev_value + 1
