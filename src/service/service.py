from src.repository.price_store import PriceStore
from src.service import model, inference_mamdani


class Service:
    def __init__(self, price_store: PriceStore):
        self.price_store = price_store
        inference_mamdani.preprocessing(model.input_lvs, model.output_lv)

    def normalize(self, x, min, max):
            """

            :param x: value in the input range
            :param min: minimum value in input range
            :param max: maximum value in input range
            :return:
            Narmalized value x in range from 0 to 1
            """
            return abs((x - min) / (max - min))


    def validate_crisp_values(self, crisp_values):
        """

        :param crisp_values: crisp values input
        :return: void
        :raises ValueError if crisp values is out of the model range
        """
        for index, value in enumerate(crisp_values):
            if value < model.input_lvs[index]['X'][0] or value > model.input_lvs[index]['X'][1] - \
                    model.input_lvs[index]['X'][2]:
                raise ValueError("Illegal argument for lv at position {index}".format(index=index))


    def normalize_distances(self, crisp_values):
        """

        :param crisp_values: crisp values input
        :return:
        Crisp values input with normalized distances to the metro and city center
        """
        metro_distance = model.distances["Kyiv"]["metro"]
        city_distance = model.distances["Kyiv"]["city"]
        return crisp_values[0], \
               self.normalize(crisp_values[1], metro_distance[0], metro_distance[1]), \
               self.normalize(crisp_values[2], city_distance[0], city_distance[1]), \
               crisp_values[3]


    def get_fuzzy_result(self, crisp_values):
        """

        :param crisp_values: crisp values input
        :return:
        Fuzzy model output in the output range provided by the price_store object
        """
        crisp_values = self.normalize_distances(crisp_values)
        self.validate_crisp_values(crisp_values)
        (crisp, word) = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp_values)
        return self.price_store.low + crisp * (self.price_store.high - self.price_store.low), word
