import time

from selenium.webdriver.common.by import By


class PriceStore:
    def __init__(self, driver):
        self.driver = driver
        (self.low, self.high) = self.get_high_and_low()

    def get_high_and_low(self):
        """
        Function uses Selenium driver to open dom.ria.com website
        and select max and min price of apartments in Kyiv with area between
        18 and 200 square meters. Minimum price should be at least 10 000 $
        as sometimes people put rental property in the "sell" category.
        :return:
        Minimum and maximum price of apartment in Kyiv
        """
        self.driver.get("https://dom.ria.com/uk/prodazha-kvartir/kiev/")

        time.sleep(1)
        self.driver.find_element(By.ID, 'mainAdditionalParams_2').click()

        element = self.driver.find_element(By.ID, '214_from')
        element.click()
        element.send_keys("18")

        element = self.driver.find_element(By.ID, '214_to')
        element.click()
        element.send_keys("200")

        time.sleep(1)
        self.driver.find_element(By.ID, 'mainAdditionalParams_2').click()

        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'span.el-select.bold-500').click()
        self.driver.find_element(By.XPATH, '//span[text()="Спочатку дорогі"]').click()

        time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR, 'b.size18')
        high = self.text_to_number(element.text)

        self.driver.find_element(By.CSS_SELECTOR, 'span.el-select.bold-500').click()
        self.driver.find_element(By.XPATH, '//span[text()="Спочатку дешеві"]').click()

        time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR, 'b.size18')
        low = self.text_to_number(element.text)
        return (low, high)

    def text_to_number(self, s):
        """
        Function transforms text from HTML element to the integer number
        and returns it, unless the number is smaller than 10 000 $, then
        10000 is returned.

        :param s: Text from HTML element with price
        :return:
        Price of apartment as number
        """
        s = s.replace("$", "")
        s = s.replace(" ", "")
        number = int(s)
        return number if number > 10000 else 10000
