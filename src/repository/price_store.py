import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class PriceStore:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.low = 0
        self.high = 0

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
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'b.size18')
        elements = map(self.text_to_number, filter(lambda s: not s.startswith("від"), map(lambda e: e.text, elements)))
        high = self.average_without_outliers(list(elements))

        self.driver.find_element(By.CSS_SELECTOR, 'span.el-select.bold-500').click()
        self.driver.find_element(By.XPATH, '//span[text()="Спочатку дешеві"]').click()

        time.sleep(3)
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'b.size18')
        elements = map(self.text_to_number, filter(lambda s: not s.startswith("від"), map(lambda e: e.text, elements)))
        low = self.average_without_outliers(list(elements))

        (self.low, self.high) = low, high

    def average_without_outliers(self, lst:list):
        if len(lst) == 0:
            return 0
        lst = list(map(lambda element: (element * .95, element * 1.05, element), lst))
        result = []
        for i in range(len(lst)):
            overlaps = False

            if 0 <= i - 1 and lst[i - 1][1] >= lst[i][0]:
                overlaps = True
            if i + 1 < len(lst) and lst[i + 1][0] <= lst[i][1]:
                overlaps = True
            if overlaps:
                result.append(lst[i][2])

        return int(sum(result) / len(result))


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
        return int(s)

