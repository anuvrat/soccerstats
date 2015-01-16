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
    referee_name = scrapy.Field()
    start_time = scrapy.Field()
    man_of_the_match = scrapy.Field()

    home_team_id = scrapy.Field()
    home_team_name = scrapy.Field()
    home_team_average_age = scrapy.Field()
    home_team_manager = scrapy.Field()
    home_team_rating = scrapy.Field()
    home_team_formation = scrapy.Field()
    home_team_players = scrapy.Field()
    home_team_score_halftime = scrapy.Field()
    home_team_score_fulltime = scrapy.Field()

    away_team_id = scrapy.Field()
    away_team_name = scrapy.Field()
    away_team_average_age = scrapy.Field()
    away_team_manager = scrapy.Field()
    away_team_rating = scrapy.Field()
    away_team_formation = scrapy.Field()
    away_team_players = scrapy.Field()
    away_team_score_halftime = scrapy.Field()
    away_team_score_fulltime = scrapy.Field()