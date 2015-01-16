# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WhoScoredRatingsItem(scrapy.Item):
    """
        Define the item that will store the player ratings for a team in a match
    """
    match_id = scrapy.Field()
    venue_name = scrapy.Field()

    team_id = scrapy.Field()
    team_name = scrapy.Field()
    team_rating = scrapy.Field()
    team_formation = scrapy.Field()
    players_rating = scrapy.Field()

    opponent_id = scrapy.Field()
    opponent_name = scrapy.Field()
    opponent_rating = scrapy.Field()
    opponent_formation = scrapy.Field()
