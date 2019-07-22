# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item
from scrapy.loader.processors import MapCompose, TakeFirst

__author__ = "aserhii@protonmail.com"


def filter_question(value):
    """"""
    if value == "?":
        return None
    return value


class CityItem(Item):
    """
    """

    country = Field()
    freedomhouse_score = Field(output_processor=TakeFirst())
    quality_of_life_index = Field(input_processor=MapCompose(filter_question))
    purchasing_power_index = Field(input_processor=MapCompose(filter_question))
    safety_index = Field(input_processor=MapCompose(filter_question))
    health_care_index = Field(input_processor=MapCompose(filter_question))
    cost_of_living_index = Field(input_processor=MapCompose(filter_question))
    property_price_to_income_ratio = Field(input_processor=MapCompose(filter_question))
    traffic_commute_time_index = Field(input_processor=MapCompose(filter_question))
    pollution_index = Field(input_processor=MapCompose(filter_question))
    climate_index = Field(input_processor=MapCompose(filter_question))
