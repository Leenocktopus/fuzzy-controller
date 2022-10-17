from unittest import TestCase
from unittest.mock import Mock

from src.repository.price_store import PriceStore


class UnitTestPriceStore(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Mock()
        cls.price_store = PriceStore(cls.driver)

    def test_average_without_outliers(self):
        lst = [10_000, 14_000, 14_000, 14_500,
               15_000, 15_600, 16_000, 16_000, 16_500, 16_500, 16_900,
               17_500, 17_500, 17_889, 18_000, 19_000, 19_000, 19_000,
               19_500, 19_700]
        expected_result = 16952
        self.assertEqual(expected_result, self.price_store.average_without_outliers(lst))

    def test_average_without_outliers_with_empty_list(self):
        lst = []
        expected_result = 0
        self.assertEqual(expected_result, self.price_store.average_without_outliers(lst))

    def test_text_to_number(self):
        s = "$ $ 392 3 2$ 32 1 45 $ $ $"
        expected_result = 3923232145
        self.assertEqual(expected_result, self.price_store.text_to_number(s))

#
# def test_normalization_with_negative_values(self):
#     source_range = (-10, 20)
#     input_value = 1
#     expected_result = .36666666666666664
#     self.assertEqual(expected_result, self.service.normalize(input_value, source_range[0], source_range[1]))
#
# def test_crisp_values_validation_size(self):
#     crisp_values = (300, .1, .1, 5)
#     self.assertRaisesRegex(ValueError, 'Illegal argument for lv at position 0', self.service.validate_crisp_values, crisp_values)
#
# def test_crisp_values_validation_proximity_to_metro(self):
#     crisp_values = (20, 1.1, .1, 5)
#     self.assertRaisesRegex(ValueError, 'Illegal argument for lv at position 1', self.service.validate_crisp_values, crisp_values)
#
# def test_crisp_values_validation_proximity_to_city_center(self):
#     crisp_values = (20, 0.2, 10.1, 5)
#     self.assertRaisesRegex(ValueError, 'Illegal argument for lv at position 2', self.service.validate_crisp_values, crisp_values)
#
# def test_crisp_values_validation_ceiling_height(self):
#     crisp_values = (20, 0.2, 0.2, 10)
#     self.assertRaisesRegex(ValueError, 'Illegal argument for lv at position 3', self.service.validate_crisp_values, crisp_values)
#
# def test_normalize_distances(self):
#     crisp_values = (20, 14, 10, 3)
#     expected_result = (20, .9333333333333333, 0.5, 3)
#     self.assertEqual(expected_result, self.service.normalize_distances(crisp_values))
#
# def test_get_fuzzy_result(self):
#     crisp_values = (30, 14, 10, 2.8)
#     expected_result = (30956.666666666668, 'cheap')
#     self.assertEqual(expected_result, self.service.get_fuzzy_result(crisp_values))
