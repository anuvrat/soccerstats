# -*- coding: utf-8 -*-

"""
Spider to crawl WhoScored web pages.
"""

import re

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
from soccerstats.spiders.whoscored_linkextractor import WhoScoredLinkExtractor
from soccerstats.items import WhoScoredRatingsItem
import json


class WhoScoredSpider(CrawlSpider):
    """
    Define the crawler to crawwl WhoScored web pages and extract player ratings
    """
    name = 'WhoScored'
    allowed_domains = ['www.whoscored.com']
    rules = (
        Rule(WhoScoredLinkExtractor(), callback='parse_item'),
    )

    def __init__(self, tournament=None, year=None, month=None, *args, **kwargs):
        super(WhoScoredSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.__prepare_seed_list(tournament, year, month)

    def parse_item(self, response):
        """
        Given the match feed page, extract ratings for both the teams
        :param response: The contents of the match page
        :return: The rating items for both the teams.
        """
        
        match_data = response.xpath('//script[contains(., "matchCentreData")]/text()').extract()[0]
        match_center_data = json.loads(re.search("matchCentreData = (.+?);", match_data).group(1))

        item = WhoScoredRatingsItem()
        item['match_id'] = re.search("matchId = (.+?);", match_data).group(1)
        
        item['venue_name'] = match_center_data['venueName']
        
        return item
        

    def __prepare_seed_list(self, tournament, year, month):
        whoscored_feed_url = get_project_settings().get('WHOSCORED_FEED_URL')

        if tournament and year and month:
            return [whoscored_feed_url % (tournament, year, month)]

        tournaments = get_project_settings().get('TOURNAMENTS')
        years = get_project_settings().get('TOURNAMENT_YEARS')

        dates = [(years[0], month) for month in xrange(06, 12)]
        dates.extend([(years[1], month) for month in xrange(01, 06)])

        return [whoscored_feed_url % (tournament, year, month) for tournament in tournaments for (year, month) in dates]
