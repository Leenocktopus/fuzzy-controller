from unittest import TestCase
from unittest.mock import Mock

from src.service.service import Service


class UnitTestService(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.price_store = Mock(low=30_000, high=100_000)
        cls.service = Service(cls.price_store)


    def test_normalization(self):
        source_range = (0, 120)
        input_value = 15
        expected_result = .125
        self.assertEqual(expected_result, self.service.normalize(input_value, source_range[0], source_range[1]))

    def test_normalization_with_negative_values(self):
        source_range = (-10, 20)
        input_value = 1
        expected_result = .36666666666666664
        self.assertEqual(expected_result, self.service.normalize(input_value, source_range[0], source_range[1]))

    def test_crisp_values_validation_size(self):
        crisp_values = (300, .1, .1, 5)
        self.assertRaisesRegex(ValueError, 'Illegal argument for lv at position 0', self.service.validate_crisp_values, crisp_values)

    def test_crisp_values_validation_proximity_to_metro(self):
        crisp_values = (20, 1.1, .1, 5)
        self.assertRaisesRegex(ValueError, 'Illegal argument for lv at position 1', self.service.validate_crisp_values, crisp_values)

    def test_crisp_values_validation_proximity_to_city_center(self):
        crisp_values = (20, 0.2, 10.1, 5)
        self.assertRaisesRegex(ValueError, 'Illegal argument for lv at position 2', self.service.validate_crisp_values, crisp_values)

    def test_crisp_values_validation_ceiling_height(self):
        crisp_values = (20, 0.2, 0.2, 10)
        self.assertRaisesRegex(ValueError, 'Illegal argument for lv at position 3', self.service.validate_crisp_values, crisp_values)

    def test_normalize_distances(self):
        crisp_values = (20, 14, 10, 3)
        expected_result = (20, .9333333333333333, 0.5, 3)
        self.assertEqual(expected_result, self.service.normalize_distances(crisp_values))

    def test_get_fuzzy_result(self):
        crisp_values = (30, 14, 10, 2.8)
        expected_result = (30956.666666666668, 'cheap')
        self.assertEqual(expected_result, self.service.get_fuzzy_result(crisp_values))
